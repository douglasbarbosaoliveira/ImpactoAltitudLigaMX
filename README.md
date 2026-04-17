# Impacto de la Altitud en la Liga MX | Altitude Impact Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Machine--Learning-Scikit--learn-orange.svg" alt="ML">
  <img src="https://img.shields.io/badge/Neural--Networks-MLP-red.svg" alt="NN">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=Streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/University-UDEM-yellow.svg" alt="UDEM">
</p>

<h3 align="center">
  🌐 <b><a href="https://ligamx-altitud.streamlit.app/">ACCESS THE LIVE DASHBOARD / ACCEDER AL SIMULADOR</a></b> 🌐
</h3>

---

## 🌎 Choose your language / Seleccione su idioma / Escolha seu idioma

<details>
<summary><b>English (EN-US) 🇺🇸</b></summary>

### 📌 Project Overview
Developed at **Universidad de Monterrey (UDEM)**, this research quantifies the "Altitude Tax" in Mexican football. By combining sports physiology with advanced Machine Learning, we analyzed 4 years of data (2021-2025) to predict how hypoxia influences competitive outcomes. The final product is a multi-language, interactive web dashboard.

### 🔬 Methodology & Evolution
1. **Statistical Foundation:** OLS Regression to isolate altitude as a key variable.
2. **Probability Mapping:** Logistic Regression to define the likelihood of scoring points.
3. **Decision Boundaries:** Identifying the exact mathematical threshold where altitude dominates the result.
4. **Model Comparison & Web App:** Deployed a Multilayer Perceptron (MLP) Neural Network via Streamlit to serve real-time predictions, discarding decision trees (Random Forest) due to clustering bias at extreme altitudes.

</details>

<details>
<summary><b>Español (ES-MX) 🇲🇽</b></summary>

### 📌 Descripción del Proyecto
Investigación desarrollada en la **Universidad de Monterrey (UDEM)** que cuantifica el "Impuesto del Oxígeno" en el fútbol mexicano. Combinando fisiología deportiva con Machine Learning avanzado, analizamos 4 años de datos (2021-2025) para predecir cómo la hipoxia influye en los resultados. El producto final es un dashboard interactivo en la nube.

### 📊 Hallazgos Clave
* **Erosión de Puntos:** Pérdida de **0.062 puntos** por cada 1,000m de ascenso (p-value: 0.0440).
* **Frontera de Decisión:** Identificación del umbral matemático exacto donde la altitud se vuelve el factor determinante.
* **Benchmark & Deploy:** Comparativa integral entre modelos y despliegue de la Red Neuronal (MLP) a través de una aplicación web construida con Streamlit.

</details>

<details>
<summary><b>Português (PT-BR) 🇧🇷</b></summary>

### 📌 Visão Geral do Projeto
Pesquisa desenvolvida na **Universidad de Monterrey (UDEM)** sobre o "Imposto do Oxigênio" no futebol mexicano. Unindo fisiologia esportiva e Machine Learning, analisamos dados de 2021 a 2025 para prever o impacto da hipóxia nos resultados. O projeto culminou na criação de um simulador web interativo.

### 🔬 Metodologia e Resultados
* **Impacto Real:** Queda de **0,062 pontos** a cada 1.000m de subida para o visitante.
* **Fronteira de Decisão:** Mapeamento do limite matemático exato onde a altitude supera o nível técnico.
* **Performance & Aplicação:** Comparação de modelos clássicos contra IA, com o deploy final do modelo de Redes Neurais (MLP) via Streamlit Cloud.

</details>

---

## 🚀 Analysis Journey | Trayectoria | Jornada

| Phase | Model | Key Visual | Insight |
| :--- | :--- | :--- | :--- |
| **1. Regression** | OLS Linear | `regresion-lineal.png` | Confirmed altitude as a significant factor (p < 0.05). |
| **2. Logit** | Logistic Reg. | `regresion-logistica.png` | Mapped the probability curve of scoring points. |
| **3. LDA Boundary** | LDA | `lda-boundary.png` | Visualized the linear separation of competitive classes. |
| **4. ML Frontiers** | Random Forest | `frontera-decision.png` | Identified non-linear thresholds and decision zones. |
| **5. Application** | **MLP & Streamlit** | **Web Dashboard** | **Deployed a real-time simulator mimicking a sports broadcast UI.** |

---

## 🖼️ Visualizations | Visualizaciones | Visualizações

<table align="center">
  <tr>
    <td align="center"><b>1. Linear Regression</b><br><img src="./visuals/regresion-lineal.png" width="300px"></td>
    <td align="center"><b>2. Logistic Probability</b><br><img src="./visuals/regresion-logistica.png" width="300px"></td>
  </tr>
  <tr>
    <td align="center"><b>3. LDA Boundary</b><br><img src="./visuals/lda-boundary.png" width="300px"></td>
    <td align="center"><b>4. ML Decision Frontier</b><br><img src="./visuals/frontera-decision.png" width="300px"></td>
  </tr>
  <tr>
    <td colspan="2" align="center"><b>5. Model Comparison (Benchmark)</b><br><img src="./visuals/comparativa-modelosAI.png" width="500px"></td>
  </tr>
</table>

---

## 📑 Interactive Reports | Reportes | Relatórios (HTML)

*Access the full technical analysis for each phase:*

* 📊 [Phase 1: Linear Regression](./pages/Altitud_LigaMX-Regresion.html)
* 📈 [Phase 2: Logistic Regression & ROC Curve](./pages/Altitud_LigaMX-Regresion_Logistica.html)
* 🧪 [Phase 3: LDA & Decision Boundaries](./pages/Altitud_LigaMX-LDA_Arboles_Decisión.html)
* 🧠 [Phase 4: Neural Networks & Ensembles](./pages/Altitud_LigaMX-Ensambles_RedesNeuronales.html)

---

## 🛠️ Tech Stack | Stack Tecnológico
- **Web App:** `Streamlit`
- **Data & Math:** `Python 3.8+`, `Pandas`, `Numpy`
- **Machine Learning:** `Scikit-learn`, `Statsmodels`
- **Visuals:** `Matplotlib`, `Seaborn`

## 📂 Structure | Estructura
* `/app.py`: Main Streamlit web application.
* `/requirements.txt`: Dependencies for Cloud Deployment.
* `/*.pkl`: Serialized Machine Learning models and scalers.
* `/logos`: Team crests for the interactive dashboard.
* `/data`: Curated Liga MX datasets.
* `/notebooks`: Source code files (.ipynb).
* `/pages`: Interactive HTML reports.
* `/visuals`: High-resolution model visualizations.

## ⚙️ Setup & Run (Local)
To run the interactive dashboard on your local machine:

```bash
# Clone the repository
git clone [https://github.com/douglasbarbosaoliveira/ImpactoAltitudLigaMX.git](https://github.com/douglasbarbosaoliveira/ImpactoAltitudLigaMX.git)
cd ImpactoAltitudLigaMX

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit App
streamlit run app.py
