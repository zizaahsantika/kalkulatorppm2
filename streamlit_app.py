import streamlit as st

st.title("Kalkulator PPM")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

st.title("Kalkulator PPM (Part Per Million)")

st.markdown("""
### Rumus:
PPM = (massa zat / massa larutan) × 10⁶
""")

# Input dari pengguna
massa_zat = st.number_input("Masukkan massa zat (dalam mg atau gram)", min_value=0.0, step=0.1)
massa_larutan = st.number_input("Masukkan massa larutan (dalam kg atau liter)", min_value=0.000001, step=0.1)

# Tombol hitung
if st.button("Hitung PPM"):
    ppm = (massa_zat / massa_larutan) * 1_000_000
    st.success(f"Nilai PPM adalah: {ppm:.2f} ppm")

# Catatan satuan
st.info("Pastikan satuan yang digunakan konsisten (misal: gram dan kg, atau mg dan liter).")
