# 🇮🇩 IndoBERT Sentiment Analysis API for Shopee Reviews

Proyek ini adalah sistem klasifikasi sentimen *end-to-end* yang dirancang untuk menganalisis ulasan pelanggan dari platform Shopee. Menggunakan arsitektur Transformer (IndoBERT) dan dideploy menggunakan FastAPI, sistem ini mampu menangani karakteristik teks informal Indonesia seperti slang, singkatan, dan *typo*.

---

## Fitur Utama
- **State-of-the-Art NLP:** Menggunakan model `IndoBERT-Sentiment-Analysis` dari Hugging Face.
- **Real-time Inference:** REST API yang cepat menggunakan FastAPI dengan dukungan asinkron.
- **Preprocessing Pipeline:** Normalisasi teks otomatis untuk menangani bahasa gaul khas *e-commerce*.
- **Batch Evaluation:** Mampu memproses ribuan data (2.900+ baris) secara otomatis menggunakan skrip evaluasi.
- **Top Sentiment Export:** Fitur untuk mengekspor ulasan dengan tingkat kepercayaan (*confidence score*) tertinggi ke dalam CSV untuk analisis kualitatif.

---

## Tech Stack
- **Framework API:** FastAPI & Uvicorn
- **Library NLP:** Hugging Face Transformers
- **Deep Learning Backend:** PyTorch / TensorFlow
- **Data Analysis:** Pandas, Scikit-Learn
- **Visualization:** Seaborn, Matplotlib

---

## Struktur Proyek
```text
review_nlp_api/
├── app/
│   ├── main.py          # Definisi endpoint FastAPI
│   ├── model.py         # Wrapper model IndoBERT & Label Mapping
│   └── utils.py         # Logika Text Preprocessing
├── data/
│   ├── data_uji.csv     # Dataset Review Shopee (Input)
│   └── slang_dict.json  # Kamus normalisasi kata slang
├── evaluate.py          # Skrip evaluasi performa model
├── export_top.py        # Skrip untuk mengambil sampel sentimen ekstrem
├── requirements.txt     # Daftar dependensi library
└── README.md
