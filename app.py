import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import os
import json
import joblib

st.set_page_config(page_title="DualPath MedAI", layout="wide", page_icon="⚕️")
st.title("⚕️ DualPath MedAI")

# --- 1. CARICAMENTO DI TUTTI GLI ASSET ---
@st.cache_resource
def load_assets():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path 1: MoA (Biologico)
    moa_model = tf.keras.models.load_model(os.path.join(current_dir, 'moa_model.h5'))
    moa_scaler = joblib.load(os.path.join(current_dir, 'moa_scaler.pkl')) # Fondamentale per le predizioni!
    
    with open(os.path.join(current_dir, 'feature_cols.json'), 'r') as f:
        moa_features = json.load(f)
    with open(os.path.join(current_dir, 'target_labels.json'), 'r') as f:
        moa_targets = json.load(f)
        
    # Path 2: Medical (Clinico)
    med_model = tf.keras.models.load_model(os.path.join(current_dir, 'medical_model.h5'))
    tfidf = joblib.load(os.path.join(current_dir, 'tfidf_vectorizer.pkl'))
    mlb = joblib.load(os.path.join(current_dir, 'mlb_binarizer.pkl'))
    
    return moa_model, moa_scaler, moa_features, moa_targets, med_model, tfidf, mlb

try:
    moa_model, moa_scaler, moa_features, moa_targets, med_model, tfidf, mlb = load_assets()
    st.success("Modelli Biologico e Clinico caricati e operativi!")
except Exception as e:
    st.error(f"Errore nel caricamento dei file: {e}")
    st.stop()

# --- 2. INTERFACCIA A SCHEDE (DUAL PATH) ---
tab1, tab2 = st.tabs(["🧬 Path 1: Analisi Biologica (MoA)", "🏥 Path 2: Analisi Clinica (Side Effects)"])

# ==========================================
# TAB 1: MODELLO BIOLOGICO
# ==========================================
with tab1:
    st.header("Predizione Meccanismo d'Azione")
    
    st.sidebar.header("Parametri Farmaco")
    cp_time = st.sidebar.selectbox("Tempo di esposizione (ore)", [24, 48, 72])
    cp_dose = st.sidebar.radio("Dosaggio", ["D1 (Basso)", "D2 (Alto)"])

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🧬 Gene Expression (g-)")
        g0 = st.slider("Espressione Genica Gruppo 1 (g0)", -10.0, 10.0, 0.0, key="g0")
        g1 = st.slider("Espressione Genica Gruppo 2 (g1)", -10.0, 10.0, 0.0, key="g1")
    with col2:
        st.markdown("### 🧫 Cell Viability (c-)")
        c0 = st.slider("Vitalità Cellulare Gruppo 1 (c0)", -10.0, 10.0, 0.0, key="c0")
        c1 = st.slider("Vitalità Cellulare Gruppo 2 (c1)", -10.0, 10.0, 0.0, key="c1")

    col_btn1, col_btn2 = st.columns(2)
    analyze_btn = col_btn1.button("Analizza Input Manuale")
    simulate_btn = col_btn2.button("Simula Farmaco Reale")

    if analyze_btn or simulate_btn:
        with st.spinner('Elaborazione biologica in corso...'):
            input_data = np.zeros((1, len(moa_features)))
            
            if simulate_btn:
                # Dati casuali realistici prima dello scaling
                input_data = np.random.uniform(-3.0, 3.0, size=(1, len(moa_features)))
            else:
                # Estrazione indici per applicare i cursori massivamente
                g_indices = [i for i, feat in enumerate(moa_features) if feat.startswith('g-')]
                c_indices = [i for i, feat in enumerate(moa_features) if feat.startswith('c-')]
                
                # Applicazione segnale: g0 alla prima metà dei geni, g1 alla seconda metà
                mid_g = len(g_indices) // 2
                for i in g_indices[:mid_g]: input_data[0, i] = g0
                for i in g_indices[mid_g:]: input_data[0, i] = g1
                
                # Applicazione segnale: c0 alla prima metà delle cellule, c1 alla seconda metà
                mid_c = len(c_indices) // 2
                for i in c_indices[:mid_c]: input_data[0, i] = c0
                for i in c_indices[mid_c:]: input_data[0, i] = c1
            
            # FASE CRITICA AGGIUNTA: Scaliamo i dati esattamente come nel training
            input_data_scaled = moa_scaler.transform(input_data)
            
            # Predizione sui dati scalati
            prediction = moa_model.predict(input_data_scaled)[0]
            results = pd.DataFrame({'Meccanismo': moa_targets, 'Probabilità': prediction}).sort_values(by='Probabilità', ascending=False)
            top_5 = results.head(5)
            
            st.subheader("🎯 Top 5 Meccanismi d'Azione")
            
            chart_data = top_5.set_index('Meccanismo')
            st.bar_chart(chart_data['Probabilità'], color="#ff4b4b")
            
            st.markdown("---")
            cols = st.columns(5)
            for idx, (index, row) in enumerate(top_5.iterrows()):
                cols[idx].metric(label=row['Meccanismo'][:15]+"...", value=f"{row['Probabilità']*100:.1f}%")

# ==========================================
# TAB 2: MODELLO CLINICO (Versione Blindata)
# ==========================================
with tab2:
    st.header("Predizione Effetti Collaterali (NLP)")
    st.markdown("Inserisci i dati clinici del farmaco per prevedere i possibili effetti avversi.")
    
    med_col1, med_col2 = st.columns(2)
    with med_col1:
        medical_condition = st.text_input("Condizione Medica (es. Acne, Diabetes)", value="Acne")
    with med_col2:
        drug_class = st.text_input("Classe del Farmaco (es. Tetracyclines)", value="Tetracyclines")
        
    if st.button("Prevedi Effetti Collaterali"):
        with st.spinner("Analisi testuale in corso..."):
            combined_text = str(medical_condition).lower() + " " + str(drug_class).lower()
            
            # Trasformazione TF-IDF
            X_med_input = tfidf.transform([combined_text]).toarray()
            
            # 1. Controllo: se l'input è sconosciuto (vettore di zeri)
            if np.all(X_med_input == 0):
                st.warning("⚠️ Termini non riconosciuti. Prova con parole come 'Acne', 'Diabetes', 'SSRIs' o 'Tetracyclines'.")
            else:
                # 2. Se i termini sono validi, procediamo con predizione e visualizzazione
                med_preds = med_model.predict(X_med_input)[0]
                
                med_results = pd.DataFrame({
                    'Effetto Collaterale': mlb.classes_,
                    'Rischio': med_preds
                }).sort_values(by='Rischio', ascending=False)
                
                st.subheader("Top 5 Effetti Collaterali Previsti")
                top_5_med = med_results.head(5)

                # Grafico (ora dentro l'else, quindi top_5_med ESISTE per forza)
                med_chart_data = top_5_med.set_index('Effetto Collaterale')
                st.bar_chart(med_chart_data['Rischio'], color="#ff4b4b")

                # Elenco dettagliato con barre di progresso
                for _, row in top_5_med.iterrows():
                    risk_val = float(row['Rischio'])
                    st.write(f"**{row['Effetto Collaterale']}**")
                    st.progress(min(risk_val, 1.0))
                    st.caption(f"Probabilità di insorgenza: {risk_val*100:.2f}%")