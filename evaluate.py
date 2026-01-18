import pandas as pd
import requests
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load Data
file_path = 'data.csv' \
df = pd.read_csv(file_path)

# 2. Fungsi untuk memanggil API
def get_prediction(text):
    url = "http://127.0.0.1:8000/predict"
    try:
        response = requests.post(url, json={"text": str(text)})
        res_json = response.json()
        return res_json['label']
    except Exception as e:
        return None

print(f"Memproses {len(df)} baris data...")
df['pred_string'] = df['ulasan'].apply(get_prediction)

# 3. Mapping Label untuk Perbandingan
# Kita ubah hasil API (string) menjadi angka (0/1) agar bisa dibandingkan dengan kolom 'label'
mapping = {
    "POSITIVE": 1,
    "NEGATIVE": 0,
}
df['pred_numeric'] = df['pred_string'].map(mapping)

# 4. Evaluasi
# Menghapus data jika ada prediksi yang gagal (None)
df_clean = df.dropna(subset=['pred_numeric'])

print("\n--- Laporan Klasifikasi ---")
# Bandingkan kolom 'label' asli dengan 'pred_numeric'
print(classification_report(df_clean['label'], df_clean['pred_numeric'], 
                            target_names=['Negative (0)', 'Positive (1)', 'Neutral (2)'][:len(df_clean['pred_numeric'].unique())]))

# 5. Visualisasi Confusion Matrix

cm = confusion_matrix(df_clean['label'], df_clean['pred_numeric'])
plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens')
plt.title('Confusion Matrix: Data Asli vs Prediksi API')
plt.ylabel('Label Asli (0/1)')
plt.xlabel('Label Prediksi Model')
plt.show()