---
marp: true
paginate: true
style: |
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
  
  section {
    background-color: #070e20;
    background-image: 
      radial-gradient(circle at 0% 0%, rgba(0, 191, 165, 0.25) 0%, transparent 40%),
      radial-gradient(circle at 100% 100%, rgba(0, 229, 255, 0.2) 0%, transparent 50%);
    color: #e0eaf5;
    font-family: 'Outfit', sans-serif;
    justify-content: flex-start;
    padding: 70px 90px;
  }
  h1 {
    color: #ffffff;
    font-size: 3.2em;
    font-weight: 700;
    text-shadow: 0 0 15px rgba(0, 191, 165, 0.4);
    border-bottom: 2px solid rgba(0, 191, 165, 0.3);
    padding-bottom: 15px;
    margin-bottom: 0.5em;
  }
  h2 {
    color: #00e5ff;
    font-weight: 500;
    font-size: 2.2em;
    margin-top: 10px;
  }
  strong {
    color: #1de9b6;
    font-weight: 700;
  }
  ul {
    line-height: 1.7;
    font-size: 1.15em;
  }
  li {
    margin-bottom: 15px;
    padding-left: 15px;
    border-left: 2px solid rgba(29, 233, 182, 0.4);
  }
---

# DualPath-MedAI

**L'Intelligenza Artificiale al servizio della Ricerca Farmaceutica.**

- **Sviluppatori:** Fabio D'alessandro, Maria Visone, Veronica Veneroso, Valerio Caria
- **Corso:** Python e Machine Learning

---

<div>
<center>

<h2>
Pipeline
</h2>

  <img
  src="image/pipeline.png" 
  width="800" height="500" 
  alt="Machine Learning Pipeline">

</center>
</div>

---

## Il Problema del Mercato

Sviluppare un nuovo farmaco richiede in media oltre 10 anni e investimenti miliardari.

Il collo di bottiglia principale? Il fallimento clinico tardivo.
Scoprire effetti collaterali imprevisti o meccanismi d'azione inefficaci durante le fasi avanzate brucia capitale, rallenta il time-to-market e mette a rischio i pazienti.

---

## La Nostra Soluzione

DualPath-MedAI è un Decision Support System (DSS) predittivo.

Offriamo alle aziende farmaceutiche uno strumento per simulare l'efficacia molecolare e prevedere i rischi clinici interamente in-silico, prima di avviare costosi trial fisici.

Un approccio a doppio binario per abbattere i costi di Ricerca e Sviluppo.

---

## La Tecnologia: Motore a Doppio Binario

Il nostro vantaggio competitivo risiede nell'unione di due domini tecnologici in un'unica piattaforma integrata:

1. **Motore Biologico (Deep Learning):** Analizza l'espressione genica per prevedere l'esatto meccanismo d'azione della molecola.
2. **Motore Clinico (NLP):** Elabora la letteratura medica tramite Natural Language Processing per mappare e anticipare oltre 1800 potenziali effetti collaterali.

---

## Il Valore per il Business

L'adozione di DualPath-MedAI genera un ritorno sull'investimento (ROI) immediato:

- **Abbattimento dei costi:** Riduzione drastica dei test in-vitro fallimentari.
- **Profilazione rapida del rischio:** Valutazione istantanea della tossicità clinica.
- **Scalabilità:** Un'architettura pronta per essere distribuita in Cloud (SaaS) e integrabile nei sistemi ERP delle case farmaceutiche.

---

## Roadmap e Prossimi Passi

Il Minimum Viable Product (MVP) è pienamente operativo e validato su dataset internazionali.

**Fase 2 (Scale-up):**

- Addestramento continuo tramite Real-World Data provenienti dai database ospedalieri.
- Rilascio di API proprietarie per l'integrazione con software di terze parti.

Siamo pronti a trasformare il modo in cui i farmaci arrivano sul mercato.
