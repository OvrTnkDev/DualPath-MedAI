# ⚕️ Presentazione: DualPath MedAI
**Sequenza Operativa dei Blocchi di Codice (Notebook)**

---

## 👤 Speaker 1: Fabio (Infrastruttura e Ingestion)
**Celle di riferimento nel Notebook:** [1] - [4] e [16]

* **Cella [1-2]:** Import delle librerie e documentazione dei dataset.
* **Cella [4]:** Caricamento del dataset MoA (`train_features.csv`).
* **Cella [16]:** Caricamento del dataset Clinico (`drugs_cleaned_dataset.xls`).
* **Cosa dire:** "Il mio compito è stato costruire la base. Ho gestito l'importazione dei dati genomici e clinici, assicurando che la pipeline fosse pronta per i due binari di analisi. Ho inoltre curato l'integrazione con Streamlit per rendere il codice un'applicazione fruibile."

---

## 👤 Speaker 2: Maria (Path 1: Biological MoA)
**Celle di riferimento nel Notebook:** [5] - [11]

* **Cella [5]:** Preprocessing (filtro `ctl_vehicle` e `QuantileTransformer`).
* **Cella [6]:** Architettura della Rete Neurale (Multi-Layer Perceptron).
* **Cella [9-11]:** Training del modello e grafici della Loss e dell'AUC.
* **Cosa dire:** "Seguendo il Path 1, ho lavorato sulle celle dalla 5 alla 11. Ho normalizzato i dati genetici e costruito una rete neurale multi-label. Come potete vedere dai grafici (Cella 11), il modello impara correttamente a distinguere i meccanismi d'azione biologici."



---

## 👤 Speaker 3: Veronica (Path 2: Clinical NLP)
**Celle di riferimento nel Notebook:** [17] - [19]

* **Cella [17]:** Pulizia dei sintomi tramite espressioni regolari (Regex).
* **Cella [18]:** Codifica dei target con `MultiLabelBinarizer`.
* **Cella [19]:** Vettorizzazione del testo medico tramite `TfidfVectorizer`.
* **Cosa dire:** "Il Path 2 inizia alla cella 17. Qui ho trasformato il linguaggio umano in dati numerici. Ho usato le Regex per pulire i sintomi e il TF-IDF per pesare l'importanza delle parole chiave mediche, creando la matrice di input per la parte clinica."



---

## 👤 Speaker 4: Valerio (Ensemble e Validation)
**Celle di riferimento nel Notebook:** [20] - [25]

* **Cella [21]:** Training della Rete Neurale per i Side Effects.
* **Cella [22, 24]:** Addestramento dei modelli Ensemble (**LightGBM** e **XGBoost**).
* **Cella [25]:** Calcolo dell'AUC finale e validazione.
* **Cosa dire:** "Dalla cella 20 alla fine, ho validato il sistema. Ho implementato modelli basati su alberi decisionali (XGBoost/LGBM) per confrontarli con la rete neurale. Ho inserito controlli di sicurezza per gestire i dati clinici sparsi, calcolando l'AUC finale per misurare l'affidabilità del sistema."



---

## 📊 Sintesi Sequenziale per la Commissione

| Fase | Speaker | Celle Notebook | Tecnologia Chiave |
| :--- | :--- | :--- | :--- |
| **Ingestion** | Fabio | 1, 4, 16 | Pandas / Streamlit |
| **Bio-Path** | Maria | 5 - 11 | QuantileTransformer / MLP |
| **NLP-Path** | Veronica | 17 - 19 | Regex / TF-IDF |
| **Ensemble** | Valerio | 20 - 25 | XGBoost / LightGBM |

---

## 🧐 Domande Critiche (Q&A Rapido)

1. **Perché la Cella 5 è vitale?** (Maria): "Perché normalizza la distribuzione dei geni, altrimenti la rete non convergerebbe."
2. **Perché la Cella 17 usa le Regex?** (Veronica): "Perché gli effetti collaterali sono scritti in modo non uniforme (virgole, punti e virgola) e vanno standardizzati."
3. **Perché il controllo 'if model is not None' nella Cella 24?** (Valerio): "Perché alcuni effetti collaterali non hanno abbastanza dati per essere addestrati; il codice lo rileva ed evita errori."