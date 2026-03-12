# ⚕️ Presentazione: DualPath MedAI
**Team:** Fabio, Maria, Veronica, Valerio

---

## 👤 Speaker 1: Fabio (Infrastruttura e Integrazione)
**Focus:** Il "Ponte" tra Dati e Utente.

* **Obiettivo del Progetto:** Abbiamo creato un sistema a doppio binario (biologico e clinico) per analizzare la sicurezza dei farmaci.
* **Data Ingestion Pipeline:** Ho gestito il caricamento di dataset eterogenei (CSV e Excel vecchi) utilizzando blocchi `try-except`. Questo assicura che il codice sia solido anche con file "sporchi" o formati non standard (TSV mascherati).
* **Integrazione Software (Frontend):** Ho sviluppato l'interfaccia in **Streamlit**. Non è solo grafica: è l'integrazione digitale che permette a un medico di interagire con i modelli muovendo cursori o inserendo testo, senza toccare una riga di codice Python.

---

## 👤 Speaker 2: Maria (Path 1: Analisi Biologica - MoA)
**Focus:** Cosa succede dentro la cellula.

* **Preprocessing:** Il cuore della preparazione è il `QuantileTransformer`. Abbiamo normalizzato i dati di espressione genica e vitalità cellulare per eliminare il "rumore" e aiutare la rete neurale a imparare meglio.
* **Architettura della Rete (MLP):** Abbiamo costruito un **Multi-Layer Perceptron** per la classificazione **Multi-Label**. 
* **Logica del Modello:** Lo strato di output ha 206 neuroni con attivazione `sigmoid`. Questo è fondamentale: ogni neurone calcola una probabilità indipendente, perché un farmaco può avere più meccanismi d'azione contemporaneamente.



---

## 👤 Speaker 3: Veronica (Path 2: Analisi Clinica e NLP)
**Focus:** L'IA che legge il linguaggio umano.

* **Vettorizzazione NLP:** Per analizzare le condizioni mediche, abbiamo usato il `TF-IDF Vectorizer`. Trasforma il testo in numeri pesando l'importanza delle parole chiave mediche.
* **Sfida delle Classi:** Prevediamo oltre **1800 effetti collaterali**. Per gestire questa complessità, abbiamo addestrato una rete neurale dedicata all'elaborazione del linguaggio naturale (NLP).
* **Validazione Input:** Abbiamo inserito un controllo vettoriale: se l'utente scrive parole senza senso (fuori dal dizionario medico), il sistema lo rileva e avvisa l'utente, evitando di generare predizioni casuali basate sul bias del modello.



---

## 👤 Speaker 4: Valerio (Ensemble Learning e Conclusioni)
**Focus:** Rigore scientifico e Scalabilità.

* **Modelli Ensemble:** Per validare le Reti Neurali, abbiamo implementato **XGBoost** e **LightGBM**. Questi modelli basati su "alberi decisionali" ci hanno permesso di confrontare le performance e scegliere la soluzione più robusta.
* **Metriche di Valutazione:** Non abbiamo usato l'Accuracy classica (fuorviante per i target multipli), ma l'**AUC (Area Under Curve)**. Ci dice quanto il modello è bravo a distinguere tra un effetto presente e uno assente.
* **Visione Futura:** L'architettura è **scalabile**. Anche se oggi lavoriamo su dataset di ricerca, il sistema è pronto per essere alimentato con Big Data ospedalieri reali, rendendo la farmacovigilanza un processo automatizzato e istantaneo.

---

## 📊 Sintesi Tecnica Finale

| Caratteristica | Path 1: Biologico | Path 2: Clinico |
| :--- | :--- | :--- |
| **Input** | Dati Genomici/Cellulari | Testo (Condizioni/Farmaci) |
| **Trasformazione** | Quantile Transformer | TF-IDF Vectorizer |
| **Algoritmo Core** | MLP Deep Learning | NLP Neural Network |
| **Target** | 206 Meccanismi d'Azione | 1827 Effetti Collaterali |