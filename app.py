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
    with open(os.path.join(current_dir, 'feature_cols.json'), 'r') as f:
        moa_features = json.load(f)
    with open(os.path.join(current_dir, 'target_labels.json'), 'r') as f:
        moa_targets = json.load(f)
        
    # Path 2: Medical (Clinico)
    med_model = tf.keras.models.load_model(os.path.join(current_dir, 'medical_model.h5'))
    tfidf = joblib.load(os.path.join(current_dir, 'tfidf_vectorizer.pkl'))
    mlb = joblib.load(os.path.join(current_dir, 'mlb_binarizer.pkl'))
    
    return moa_model, moa_features, moa_targets, med_model, tfidf, mlb

try:
    moa_model, moa_features, moa_targets, med_model, tfidf, mlb = load_assets()
    st.success("Modelli Biologico e Clinico caricati e operativi!")
except Exception as e:
    st.error(f"Errore nel caricamento dei file: {e}")
    st.stop()

# --- 2. INTERFACCIA A SCHEDE (DUAL PATH) ---
tab1, tab2 = st.tabs(["🧬 Path 1: Analisi Biologica (MoA)", "🏥 Path 2: Analisi Clinica (Side Effects)"])

# ==========================================
# TAB 1: MODELLO BIOLOGICO (Quello già fatto)
# ==========================================
with tab1:
    st.header("Predizione Meccanismo d'Azione")
    
    st.sidebar.header("Parametri Farmaco")
    cp_time = st.sidebar.selectbox("Tempo di esposizione (ore)", [24, 48, 72])
    cp_dose = st.sidebar.radio("Dosaggio", ["D1 (Basso)", "D2 (Alto)"])

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🧬 Gene Expression (g-)")
        g0 = st.slider("g-0", -10.0, 10.0, 0.0, key="g0")
        g1 = st.slider("g-1", -10.0, 10.0, 0.0, key="g1")
    with col2:
        st.markdown("### 🧫 Cell Viability (c-)")
        c0 = st.slider("c-0", -10.0, 10.0, 0.0, key="c0")
        c1 = st.slider("c-1", -10.0, 10.0, 0.0, key="c1")

    col_btn1, col_btn2 = st.columns(2)
    analyze_btn = col_btn1.button("Analizza Input Manuale")
    simulate_btn = col_btn2.button("Simula Farmaco Reale")

    if analyze_btn or simulate_btn:
        with st.spinner('Elaborazione biologica in corso...'):
            input_data = np.zeros((1, len(moa_features)))
            
            def set_feat(name, val):
                if name in moa_features:
                    input_data[0, moa_features.index(name)] = val

            if simulate_btn:
                input_data = np.random.uniform(-3.0, 3.0, size=(1, len(moa_features)))
            else:
                set_feat('cp_time', cp_time / 72.0)
                set_feat('cp_dose', 0 if cp_dose == "D1 (Basso)" else 1)
                
                # TRUCCO DEL BROADCASTING: Amplifichiamo il segnale degli slider
                # Applichiamo il valore del cursore a blocchi di 50 geni/cellule
                for i in range(50):
                    set_feat(f'g-{i}', g0)
                    set_feat(f'g-{i+50}', g1)
                    set_feat(f'c-{i}', c0)
                    set_feat(f'c-{i+50}', c1)
            
            prediction = moa_model.predict(input_data)[0]
            results = pd.DataFrame({'Meccanismo': moa_targets, 'Probabilità': prediction}).sort_values(by='Probabilità', ascending=False)
            top_5 = results.head(5)
            
            st.subheader("🎯 Top 5 Meccanismi d'Azione")
            
            # UPGRADE VISIVO: Grafico a barre nativo di Streamlit
            # Riformattiamo i dati per il grafico
            chart_data = top_5.set_index('Meccanismo')
            st.bar_chart(chart_data['Probabilità'], color="#ff4b4b")
            
            # Mostriamo anche i valori precisi in colonne
            st.markdown("---")
            cols = st.columns(5)
            for idx, (index, row) in enumerate(top_5.iterrows()):
                cols[idx].metric(label=row['Meccanismo'][:15]+"...", value=f"{row['Probabilità']*100:.1f}%")

# ==========================================
# TAB 2: MODELLO CLINICO (La Novità!)
# ==========================================
with tab2:
    st.header("Predizione Effetti Collaterali (NLP)")
    st.markdown("Inserisci i dati clinici del farmaco per prevedere i possibili effetti avversi.")
    
    med_col1, med_col2 = st.columns(2)
    with med_col1:
        # Esempi di test: 'Acne', 'Depression', 'High Blood Pressure'
        medical_condition = st.text_input("Condizione Medica (es. Acne, Diabetes)", value="Acne")
    with med_col2:
        # Esempi di test: 'Tetracyclines', 'SSRIs'
        drug_class = st.text_input("Classe del Farmaco (es. Tetracyclines)", value="Tetracyclines")
        
    if st.button("Prevedi Effetti Collaterali"):
        with st.spinner("Analisi testuale in corso..."):
            # 1. Combiniamo il testo esattamente come nel notebook
            combined_text = str(medical_condition) + " " + str(drug_class)
            
            # 2. Vettorizziamo con il TF-IDF salvato
            X_med_input = tfidf.transform([combined_text]).toarray()
            
            # 3. Facciamo la predizione
            med_preds = med_model.predict(X_med_input)[0]
            
            # 4. Recuperiamo i nomi degli effetti dal MultiLabelBinarizer
            med_results = pd.DataFrame({
                'Effetto Collaterale': mlb.classes_,
                'Rischio': med_preds
            }).sort_values(by='Rischio', ascending=False)
            
            st.subheader("Top 5 Effetti Collaterali Previsti")
            top_5_med = med_results.head(5)

            # Grafico riepilogativo dei primi 5 effetti collaterali
            med_chart_data = top_5_med.set_index('Effetto Collaterale')
            st.bar_chart(med_chart_data['Rischio'], color="#ff4b4b")

            for _, row in top_5_med.iterrows():
                risk_val = float(row['Rischio'])
                st.write(f"**{row['Effetto Collaterale']}**")
                
                # Colore barra in base al rischio (rosso se > 50%)
                st.progress(min(risk_val, 1.0))
                st.caption(f"Probabilità di insorgenza: {risk_val*100:.2f}%")