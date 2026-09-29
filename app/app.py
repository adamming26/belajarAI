import streamlit as st
import pandas as pd
import joblib
import os

# === KONFIGURASI HALAMAN ===
st.set_page_config(
    page_title="Prediksi Cuaca Sulawesi Tenggara",
    page_icon="🌦️",
    layout="centered"
)

# === LOAD MODEL ===
@st.cache_resource
def load_model():
    """Load model yang sudah ditraining"""
    model_path = os.path.join(
        os.path.dirname(__file__), 
        '..', 'data', 'processed', 'model_prediksi_hujan.pkl'
    )
    return joblib.load(model_path)

model = load_model()

# === FITUR ===
fitur = ['suhu_min', 'suhu_max', 'suhu_rata', 
         'kelembapan', 'penyinaran', 'kecepatan_angin']

# === JUDUL APLIKASI ===
st.title("🌦️ Prediksi Cuaca Sulawesi Tenggara")
st.markdown("Aplikasi prediksi **hujan / tidak hujan** berdasarkan data cuaca harian.")
st.markdown("---")

# === FORM INPUT ===
st.subheader("📝 Input Data Cuaca")
st.markdown("Masukkan kondisi cuaca yang ingin diprediksi:")

col1, col2 = st.columns(2)

with col1:
    suhu_min = st.number_input("Suhu Minimum (°C)", min_value=15.0, max_value=40.0, value=24.0, step=0.1)
    suhu_max = st.number_input("Suhu Maximum (°C)", min_value=15.0, max_value=45.0, value=32.0, step=0.1)
    suhu_rata = st.number_input("Suhu Rata-rata (°C)", min_value=15.0, max_value=40.0, value=27.0, step=0.1)

with col2:
    kelembapan = st.number_input("Kelembapan (%)", min_value=0.0, max_value=100.0, value=85.0, step=0.1)
    penyinaran = st.number_input("Penyinaran Matahari (jam)", min_value=0.0, max_value=15.0, value=2.0, step=0.1)
    angin = st.number_input("Kecepatan Angin (m/s)", min_value=0.0, max_value=20.0, value=1.5, step=0.1)

st.markdown("---")

# === TOMBOL PREDIKSI ===
if st.button("🔮 Prediksi Sekarang", type="primary", use_container_width=True):
    # Bikin DataFrame input
    data_input = pd.DataFrame({
        'suhu_min': [suhu_min],
        'suhu_max': [suhu_max],
        'suhu_rata': [suhu_rata],
        'kelembapan': [kelembapan],
        'penyinaran': [penyinaran],
        'kecepatan_angin': [angin]
    })[fitur]
    
    # Prediksi
    prediksi = model.predict(data_input)[0]
    probabilitas = model.predict_proba(data_input)[0]
    
    # Tampilkan hasil
    st.markdown("---")
    st.subheader("🎯 Hasil Prediksi")
    
    if prediksi == 1:
        st.error(f"### 🌧️ HUJAN")
        st.write(f"**Probabilitas Hujan:** {probabilitas[1]*100:.1f}%")
        st.write(f"**Probabilitas Tidak Hujan:** {probabilitas[0]*100:.1f}%")
        
        if probabilitas[1] > 0.7:
            st.success("☔ Rekomendasi: **Bawa payung!** Kemungkinan hujan sangat tinggi.")
        else:
            st.info("🌂 Rekomendasi: Siapkan payung, mungkin hujan.")
    else:
        st.success(f"### ☀️ TIDAK HUJAN")
        st.write(f"**Probabilitas Hujan:** {probabilitas[1]*100:.1f}%")
        st.write(f"**Probabilitas Tidak Hujan:** {probabilitas[0]*100:.1f}%")
        
        if probabilitas[1] < 0.3:
            st.success("😎 Rekomendasi: **Aman!** Cuaca cerah, tidak perlu payung.")
        else:
            st.info("🌤️ Rekomendasi: Cuaca mungkin cerah, tapi tetap waspada.")
    
    # Tampilkan detail probabilitas
    st.markdown("---")
    st.subheader("📊 Detail Probabilitas")
    prob_df = pd.DataFrame({
        'Kondisi': ['Tidak Hujan', 'Hujan'],
        'Probabilitas': [probabilitas[0], probabilitas[1]]
    })
    st.bar_chart(prob_df.set_index('Kondisi'))

# === FOOTER ===
st.markdown("---")
st.caption("Dibuat dengan dalam keadaan asam lambung")
st.caption("Model akurasi testing: 73.57%")