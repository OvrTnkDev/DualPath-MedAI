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

---
# ⚕️ Progetto DualPath-MedAI
**Framework Integrato di Intelligenza Artificiale per l'Analisi Farmacologica**

---

## 🚀 Visione del Progetto
DualPath-MedAI è una piattaforma di analisi predittiva che opera su due livelli distinti ma complementari del settore farmaceutico:
1. **Livello Molecolare:** Predizione dei Meccanismi d'Azione (MoA).
2. **Livello Clinico:** Analisi degli Effetti Collaterali tramite NLP.

---

## 👤 Speaker 1: Fabio (Software Architecture & Data Ingestion)
> *"Il ponte tra il dato grezzo e l'utente finale."*

* **Data Ingestion:** Sviluppo di una pipeline robusta per il caricamento di dataset eterogenei (CSV/Excel) con gestione degli errori tramite blocchi `try-except`.
* **System Integration:** Trasformazione del modello da semplice script a prodotto digitale tramite **Streamlit**.
* **Interfaccia Utente:** Progettazione di un sistema di input dinamico per simulare dosaggi, tempi di esposizione e sintomi clinici in tempo reale.

---

## 👤 Speaker 2: Maria (Path 1: Analisi Biologica MoA)
> *"Decodificare la risposta cellulare."*

* **Preprocessing Genomico:** Utilizzo del `QuantileTransformer` per mappare le feature (geni e cellule) su una distribuzione normale, eliminando il rumore statistico.
* **Architettura MLP:** Implementazione di una rete neurale **Multi-Label**.
* **Sigmoid Activation:** Ogni target (206 classi) viene trattato come una probabilità indipendente, permettendo al modello di rilevare attivazioni multiple simultanee.



---

## 👤 Speaker 3: Veronica (Path 2: Analisi Clinica NLP)
> *"Trasformare il linguaggio naturale in segnale digitale."*

* **Data Cleaning:** Estrazione e pulizia dei sintomi tramite **Espressioni Regolari (Regex)** per gestire le diverse nomenclature cliniche.
* **Feature Engineering:** Implementazione del **TF-IDF Vectorizer** (500 feature) per pesare l'importanza semantica delle condizioni mediche.
* **MultiLabelBinarizer:** Trasformazione di oltre 1800 effetti collaterali in una matrice binaria per l'addestramento della rete neurale clinica.



---

## 👤 Speaker 4: Valerio (Ensemble Modeling & Validation)
> *"Garantire la robustezza scientifica del sistema."*

* **Ensemble Learning:** Integrazione di modelli **XGBoost** e **LightGBM** come validatori esterni del Path 1 e Path 2.
* **Safe-Training Protocol:** Implementazione di filtri di sicurezza per gestire target "sparsi" (modelli creati solo su target con dati sufficienti).
* **Metriche di Valutazione:** Analisi delle performance tramite **AUC (Area Under Curve)**, assicurando che il modello distingua correttamente tra segnale e rumore anche in condizioni di sbilanciamento delle classi.



---

## 🛠️ Stack Tecnologico

| Componente | Tecnologia | Funzione |
| :--- | :--- | :--- |
| **Linguaggio** | Python 3.x | Core development |
| **Deep Learning** | Keras / TensorFlow | Reti Neurali MLP |
| **NLP** | Scikit-Learn (TF-IDF) | Vettorizzazione testo |
| **Boosting** | XGBoost / LightGBM | Ensemble Validation |
| **Frontend** | Streamlit | UI & Deployment |

---

---

## 🎯 Conclusioni
DualPath-MedAI dimostra come l'integrazione di **Deep Learning** e **NLP** possa accelerare lo screening farmaceutico pre-clinico. Il sistema è intrinsecamente scalabile e pronto per l'integrazione con Big Data ospedalieri e database farmaceutici aziendali.

---

# 🧐 Glossario delle "Domande Bastarde" (e come rispondere)

Questo documento contiene le risposte tecniche alle domande più probabili della commissione. Leggetele bene per non farvi trovare impreparati.

---

### 👤 Per Fabio (Infrastruttura e Integrazione)

**Domanda:** "Vedo che carichi i modelli con `@st.cache_resource`. Perché è fondamentale in un'app aziendale?"
* **Risposta Pro:** "Perché i modelli pesano centinaia di MB. Senza la cache, Streamlit ricaricherebbe i file `.h5` e `.pkl` a ogni interazione (ogni volta che l'utente muove un cursore). Questo saturerebbe la RAM e renderebbe l'app lentissima. Con la cache, il modello resta in memoria ed è pronto all'uso istantaneo."

**Domanda:** "Perché hai usato un blocco `try-except` proprio nel caricamento dei dati?"
* **Risposta Pro:** "Perché i dataset clinici spesso arrivano da fonti diverse (ospedali o database pubblici) con encoding o delimitatori diversi (es. virgole vs tabulazioni). Il `try-except` permette al software di essere resiliente: se il formato standard fallisce, il sistema prova automaticamente un'alternativa senza crashare davanti all'utente."

---

### 👤 Per Maria (Path 1: Biologia e Deep Learning)

**Domanda:** "Perché hai scelto la funzione di attivazione `sigmoid` nell'ultimo strato e non la `softmax`?"
* **Risposta Pro:** "Questa è una classificazione **Multi-Label**, non Multi-Class. Un farmaco può avere più Meccanismi d'Azione (MoA) contemporaneamente. La `softmax` costringe la somma delle probabilità a 1 (una sola risposta giusta), mentre la `sigmoid` permette a ogni neurone di dare una probabilità indipendente tra 0 e 1."

**Domanda:** "A cosa serve il `Dropout(0.3)` che hai inserito tra gli strati?"
* **Risposta Pro:** "È una tecnica di regolarizzazione per contrastare l'**Overfitting**. Durante l'addestramento, 'spegniamo' casualmente il 30% dei neuroni. Questo impedisce alla rete di memorizzare i dati a memoria e la costringe a imparare pattern generali, migliorando la capacità del modello di rispondere a dati nuovi."

---

### 👤 Per Veronica (Path 2: NLP e Vettorizzazione)

**Domanda:** "Il `TF-IDF` non è una tecnica un po' superata rispetto ai Transformer (BERT)? Perché usarla qui?"
* **Risposta Pro:** "Per due motivi: efficienza e scarsità di dati. I Transformer richiedono enormi quantità di testo per essere efficaci. In questo contesto aziendale, dove abbiamo termini medici specifici e brevi, il `TF-IDF` è estremamente veloce, leggero e ci permette di pesare l'importanza di parole chiave rare che sono fondamentali per la diagnosi clinica."

**Domanda:** "Cosa succede se inserisco un sintomo che non è presente nel dataset?"
* **Risposta Pro:** "Il sistema è protetto. Se il testo inserito non produce alcun match nel vocabolario del `TfidfVectorizer`, il vettore risultante sarà composto da soli zeri. Abbiamo implementato un controllo che rileva questa condizione (vettore nullo) e avvisa l'utente che il termine non è riconosciuto, evitando di fornire una predizione basata solo sul bias statistico."

---

### 👤 Per Valerio (Ensemble e Validazione)

**Domanda:** "L'AUC del Path 2 è molto più bassa del Path 1. Il modello è un fallimento?"
* **Risposta Pro:** "Assolutamente no. L'AUC inferiore riflette la **scarsità dei dati clinici** (circa 250 campioni contro migliaia del Path 1). Il valore del progetto non è solo nella precisione attuale, ma nell'**architettura software**: abbiamo dimostrato che la pipeline NLP funziona. Alimentando il sistema con un dataset ospedaliero più vasto, le performance saliranno senza dover modificare una singola riga di codice."

**Domanda:** "Perché usare XGBoost e LightGBM se avevate già la Rete Neurale?"
* **Risposta Pro:** "È una tecnica di **Cross-Validation algoritmica**. Le Reti Neurali sono potenti ma sono 'black boxes'. I modelli basati su alberi (XGBoost) ci permettono di verificare se il segnale trovato dalla rete è coerente. Se entrambi i modelli concordano, la nostra fiducia nella predizione clinica è molto più alta."

---

### 💡 Il consiglio finale (Peffozza!)
Se il prof vi chiede: **"Cosa fareste per migliorare il progetto?"**
Rispondete: *"Utilizzeremmo l'Ensemble Learning non solo per confronto, ma per creare un modello **Stacking**, dove la Rete Neurale e XGBoost lavorano insieme per produrre un'unica predizione finale ancora più accurata."*