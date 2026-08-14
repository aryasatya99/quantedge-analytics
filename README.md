# 📈 QuantEdge Analytics: Portfolio & Risk Analysis Pipeline

Proyek ini adalah sistem analisis risiko dan performa saham *Big-Cap* di Bursa Efek Indonesia (BEI) berbasis Python. Sistem ini mengambil data historis *real-time* dari Yahoo Finance API, mengolah metrik statistik risiko harian, dan memvisualisasikan perbandingan pertumbuhan saham secara ter-normalisasi (*Base 100*).

---

## 🛠️ Tech Stack & Tools
- **Bahasa Pemrograman:** Python 3
- **Data Manipulation:** Pandas
- **Data Source:** yFinance (Yahoo Finance API)
- **Data Visualization:** Matplotlib

---

## 📁 Struktur Workspace
```text
quantedge-analytics/
├── README.md                      # Dokumentasi Utama Proyek
├── requirements.txt               # Daftar Library Python
├── .gitignore                     # Git Exclusion Rules
├── docs/                          # Project Report & PDF Docs
├── outputs/                       # Export Grafik (.png) & Data (.csv)
└── src/
    ├── fase1_basics/              # Logic & Basic Python (Stock, Portfolio, Risk Calc)
    └── fase2_data_science/        # Data Science Pipeline (yFinance, Pandas, Matplotlib)