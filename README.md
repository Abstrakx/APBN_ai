# ⚡ APBN_ai

> **AI-Powered Building Energy Anomaly Detection & Optimization for Urban Resilience**

AI-powered platform for predicting building energy consumption, detecting anomalies, and providing actionable energy-saving recommendations for government buildings in Jakarta, Indonesia.

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Azure ML](https://img.shields.io/badge/Azure-ML%20%7C%20Maps%20%7C%20App%20Service-0078D4?logo=microsoftazure)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Problem Statement

Government buildings in DKI Jakarta consume **1,396.61 GWh of electricity per year** — accounting for **28% of all government building electricity consumption in Indonesia** (PLN Statistics 2022). With a potential energy savings of **10-30%** (Ministry of ESDM), Jakarta could save **Rp195-587 billion annually** through AI-driven energy optimization.

## 🏗️ Architecture

```
┌──────────────────────────────────────────────────────────┐
│                    APBN_ai                         │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  📊 Data Layer                                           │
│  ├── BDG2 Dataset (53.6M hourly records, 1,636 buildings)│
│  ├── Jakarta Weather (Open-Meteo Historical API)         │
│  ├── Building Metadata (51 govt buildings, coordinates)  │
│  └── PLN Statistics 2022 (validation data)               │
│                                                          │
│  🤖 ML Pipeline (Azure ML)                               │
│  ├── Energy Forecasting (LightGBM)                       │
│  ├── Anomaly Detection (Isolation Forest)                │
│  └── Building Clustering (K-Means)                       │
│                                                          │
│  🗺️ Dashboard (Azure App Service)                        │
│  ├── Interactive Azure Maps (per-building pins)          │
│  ├── IKE Efficiency Scoring & Color Coding               │
│  ├── AI Recommendations Panel                            │
│  └── ROI Calculator                                      │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

## 📊 Data Sources

| Dataset                                                                                                    | Source                          | License       |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------- | ------------- |
| [Building Data Genome Project 2](https://www.kaggle.com/datasets/claytonmiller/buildingdatagenomeproject2) | Kaggle / Nature Scientific Data | CC BY-SA 4.0  |
| [Open-Meteo Historical Weather](https://open-meteo.com/en/docs/historical-weather-api)                     | Open-Meteo API                  | CC BY 4.0     |
| [Jakarta Building Metadata](data/jakarta_government_buildings.csv)                                         | OpenStreetMap + DJKN            | ODbL / Public |
| PLN Statistics 2022                                                                                        | PT PLN (Persero)                | Public        |
| IKE Standards                                                                                              | Permen ESDM No. 13/2012         | Public        |

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/abstrakx/energikota-ai.git
cd energikota-ai

# Install dependencies
pip install -r requirements.txt

# Download BDG2 dataset (place in data/bdg2/)
# https://www.kaggle.com/datasets/claytonmiller/buildingdatagenomeproject2

# Run EDA prototype
python notebooks/01_eda_prototype.py

# Run dashboard
streamlit run src/dashboard.py
```

## 📁 Project Structure

```
datathon/
├── README.md
├── requirements.txt
├── data/
│   ├── jakarta_government_buildings.csv   # 51 govt buildings with coordinates
│   └── bdg2/                              # BDG2 dataset (download from Kaggle)
├── notebooks/
│   └── 01_eda_prototype.py                # EDA + ML pipeline prototype
├── src/
│   └── dashboard.py                       # Streamlit dashboard with Azure Maps
└── docs/
    └── proposal.md                        # Competition proposal
```

## 🔬 Methodology

1. **Train** ML models on BDG2 dataset (53.6M hourly energy readings from 1,636 buildings worldwide)
2. **Contextualize** to Jakarta's tropical climate using Open-Meteo weather data
3. **Predict** baseline energy consumption for 51 government buildings
4. **Score** each building using Indonesian IKE standards (kWh/m²/year)
5. **Validate** total predictions against PLN aggregate data (1,396.61 GWh)
6. **Visualize** on Azure Maps with efficiency color coding

## 🏆 Competition

**AI Impact Challenge — Datathon** by Microsoft Elevate Training Center × Dicoding Indonesia

- **Theme:** Urban Resilience & Smart City
- **Azure Services:** Azure ML, Azure Maps, Azure App Service, Azure Blob Storage

## 📚 References

1. Miller, C., et al. (2020). _The Building Data Genome Project 2_. Scientific Data, Nature. DOI: [10.1038/s41597-020-00712-x](https://doi.org/10.1038/s41597-020-00712-x)
2. PP No. 33 Tahun 2023 — Konservasi Energi
3. GlobalABC Indonesia Roadmap — Building Energy Efficiency for NZE 2060
