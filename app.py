import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd
import os
import json

# Configurazione Pagina
st.set_page_config(page_title="DualPath MedAI", layout="wide")
st.title("🧬 DualPath MedAI: MoA Prediction")

# 1. Caricamento Modello e Meta-dati
@st.cache_resource
def load_assets():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Percorsi file
    model_path = os.path.join(current_dir, 'moa_model.h5')
    feat_path = os.path.join(current_dir, 'feature_cols.json')
    target_path = os.path.join(current_dir, 'target_labels.json')
    
    # Caricamento
    model = tf.keras.models.load_model(model_path)
    with open(feat_path, 'r') as f:
        feature_cols = json.load(f)
    with open(target_path, 'r') as f:
        target_labels = json.load(f)
        
    return model, feature_cols, target_labels

try:
    model, feature_cols, target_labels = load_assets()
    st.success(f"Modello e {len(feature_cols)} feature caricati correttamente!")
except Exception as e:
    st.error(f"Errore nel caricamento: {e}")
    st.info("Assicurati di aver eseguito le celle di salvataggio nel Notebook!")
    st.stop()

# 2. Layout Input
st.subheader("Inserimento Parametri Biologici")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🧬 Gene Expression (g-)")
    g0 = st.slider("g-0", -10.0, 10.0, 0.0)
    g1 = st.slider("g-1", -10.0, 10.0, 0.0)
    g2 = st.slider("g-2", -10.0, 10.0, 0.0)
    g3 = st.slider("g-3", -10.0, 10.0, 0.0)
    g4 = st.slider("g-4", -10.0, 10.0, 0.0)

with col2:
    st.markdown("### 🧫 Cell Viability (c-)")
    c0 = st.slider("c-0", -10.0, 10.0, 0.0)
    c1 = st.slider("c-1", -10.0, 10.0, 0.0)
    c2 = st.slider("c-2", -10.0, 10.0, 0.0)
    c3 = st.slider("c-3", -10.0, 10.0, 0.0)
    c4 = st.slider("c-4", -10.0, 10.0, 0.0)

# 3. Costruzione Vettore di Input (DINAMICA)
# Creiamo un vettore di zeri della lunghezza esatta richiesta dal modello
input_data = np.zeros((1, len(feature_cols)))

# Funzione per mappare i valori degli slider nelle posizioni corrette
def set_feat(name, val):
    if name in feature_cols:
        idx = feature_cols.index(name)
        input_data[0, idx] = val

# Inseriamo i valori degli slider nelle colonne giuste
set_feat('g-0', g0); set_feat('g-1', g1); set_feat('g-2', g2); set_feat('g-3', g3); set_feat('g-4', g4)
set_feat('c-0', c0); set_feat('c-1', c1); set_feat('c-2', c2); set_feat('c-3', c3); set_feat('c-4', c4)

# 4. Predizione e Visualizzazione
if st.button("🔬 Analizza Meccanismo d'Azione"):
    prediction = model.predict(input_data)[0]
    
    results = pd.DataFrame({
        'Meccanismo': target_labels,
        'Probabilità': prediction
    }).sort_values(by='Probabilità', ascending=False)
    
    st.subheader("🎯 Top 5 Predizioni")
    
    # Mostriamo i primi 5 a prescindere dal valore
    for _, row in results.head(5).iterrows():
        val = float(row['Probabilità'])
        st.write(f"**{row['Meccanismo']}**")
        st.progress(min(val * 10, 1.0)) # Moltiplichiamo x10 la barra solo per vederla muovere nel test
        st.caption(f"Probabilità calcolata: {val*100:.4f}%")