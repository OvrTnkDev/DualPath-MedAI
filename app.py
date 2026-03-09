import streamlit as st
import tensorflow as tf
import numpy as np
import pandas as pd

# Configurazione pagina
st.set_page_config(page_title="DualPath MedAI", layout="wide")

st.title("🧬 DualPath MedAI: MoA Prediction")
st.markdown("Analisi dei Meccanismi d'Azione tramite Deep Learning")

# 1. Caricamento del Modello (usiamo la cache per non ricaricarlo a ogni click)
@st.cache_resource
def load_my_model():
    return tf.keras.models.load_model('moa_model.h5')

model = load_my_model()

st.success("Modello Keras caricato correttamente!")

# 2. Area di Input (Simulazione)
st.sidebar.header("Parametri Farmaco")
cp_time = st.sidebar.selectbox("Tempo di esposizione (ore)", [24, 48, 72])
cp_dose = st.sidebar.radio("Dosaggio", ["D1 (Basso)", "D2 (Alto)"])

st.info("Configurazione completata. Pronto per ricevere i dati dei geni e delle cellule.")