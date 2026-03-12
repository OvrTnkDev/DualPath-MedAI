# ⚕️ Presentazione: DualPath MedAI
**Framework Integrato di IA per l'Analisi Farmacologica**
**Team:** Fabio, Maria, Veronica, Valerio

---

## 🚀 Visione del Progetto (Intro Generale)
DualPath-MedAI analizza la sicurezza dei farmaci su due livelli complementari:
1. **Livello Molecolare:** Predizione dei Meccanismi d'Azione (MoA).
2. **Livello Clinico:** Analisi degli Effetti Collaterali tramite NLP.

---

## 👤 Speaker 1: Fabio (Infrastruttura e Ingestion)
> **[INIZIO INTERVENTO]**
> *Focus: Il ponte tra il dato grezzo e l'utente.*

* **Data Ingestion:** Sviluppo di una pipeline robusta per il caricamento di dataset eterogenei (CSV/Excel) con gestione degli errori tramite blocchi `try-except`.
* **Integrazione Software:** Trasformazione dello script di ricerca in un prodotto digitale accessibile tramite **Streamlit**.
* **Interfaccia Utente:** Progettazione di un sistema di input dinamico per simulare dosaggi e sintomi clinici in tempo reale senza scrivere codice.



> **[FINE INTERVENTO - Passa la parola a Maria]**

---

## 👤 Speaker 2: Maria (Path 1: Analisi Biologica MoA)
> **[INIZIO INTERVENTO]**
> *Focus: Decodificare la risposta cellulare.*

* **Preprocessing Genomico:** Utilizzo del `QuantileTransformer` per mappare le feature su una distribuzione normale, eliminando il rumore statistico dei campioni genetici.
* **Architettura MLP:** Implementazione di una rete neurale **Multi-Layer Perceptron** per la classificazione **Multi-Label**.
* **Sigmoid Activation:** Ogni target (206 classi) viene trattato come una probabilità indipendente, permettendo al modello di rilevare attivazioni biologiche multiple simultanee.



> **[FINE INTERVENTO - Passa la parola a Veronica]**

---

## 👤 Speaker 3: Veronica (Path 2: Analisi Clinica NLP)
> **[INIZIO INTERVENTO]**
> *Focus: Trasformare il linguaggio naturale in segnale digitale.*

* **Data Cleaning:** Estrazione dei sintomi tramite **Regex** per gestire le diverse nomenclature cliniche degli effetti collaterali.
* **Feature Engineering:** Implementazione del **TF-IDF Vectorizer** (500 feature) per pesare l'importanza semantica delle condizioni mediche inserite dall'utente.
* **Robustezza:** Integrazione di un sistema di validazione che rileva input "Out-of-Distribution" (parole non mediche), evitando predizioni casuali.



> **[FINE INTERVENTO - Passa la parola a Valerio]**

---

## 👤 Speaker 4: Valerio (Ensemble e Validazione)
> **[INIZIO INTERVENTO]**
> *Focus: Garantire la robustezza scientifica e scalabilità.*

* **Ensemble Learning:** Integrazione di modelli **XGBoost** e **LightGBM** come validatori esterni per confrontare le performance delle Reti Neurali.
* **Safe-Training:** Filtri di sicurezza per gestire target clinici "sparsi", assicurando che ogni modello addestrato abbia una base statistica valida.
* **Metriche:** Utilizzo dell'**AUC (Area Under Curve)** come metrica principale per valutare la capacità discriminante del modello su classi sbilanciate.



> **[FINE INTERVENTO - Conclusioni Finali]**

---

## 📊 Sintesi Tecnica Finale

| Caratteristica | Path 1: Biologico | Path 2: Clinico |
| :--- | :--- | :--- |
| **Input Data** | Dati Genomici/Cellulari | Testo Libero (Condizioni) |
| **Preprocessing** | Quantile Transformer | TF-IDF Vectorizer |
| **Algoritmo Core** | MLP Deep Learning | NLP Neural Network |
| **Target** | 206 Meccanismi d'Azione | 1827 Effetti Collaterali |

---

## 🧐 Glossario delle "Domande Bastarde" (Q&A)

### 👤 Per Fabio (Infrastruttura)
* **Q:** Perché carichi i modelli con `@st.cache_resource`?
* **A:** Per efficienza. I modelli pesano centinaia di MB; senza cache, l'app ricaricherebbe tutto a ogni click, saturando la RAM e diventando lentissima.

### 👤 Per Maria (Biologia)
* **Q:** Perché la Sigmoid e non la Softmax nell'ultimo strato?
* **A:** Perché è un problema Multi-Label. Un farmaco può avere più MoA insieme. La Softmax ne sceglierebbe solo uno, la Sigmoid dà probabilità indipendenti per ognuno.

### 👤 Per Veronica (NLP)
* **Q:** Perché usare TF-IDF e non modelli più moderni come BERT?
* **A:** Per la velocità e la scarsità di dati. TF-IDF è estremamente efficiente su termini medici brevi e specifici, dove i modelli pesanti come BERT rischierebbero l'overfitting.

### 👤 Per Valerio (Validazione)
* **Q:** L'AUC clinico è più basso del biologico. È un errore?
* **A:** No, riflette la scarsità di dati pubblici sugli effetti collaterali. L'architettura è scalabile: con dataset ospedalieri più grandi, le performance salirebbero senza cambiare codice.

---

## 🎯 Conclusioni
DualPath-MedAI dimostra come l'integrazione di **Deep Learning** e **NLP** possa accelerare lo screening farmaceutico. Il sistema è intrinsecamente scalabile e pronto per l'integrazione con Big Data ospedalieri reali.