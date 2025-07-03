import streamlit as st
from datetime import time

st.title("IP Aktivite ve Site Analiz Arayüzü")

# Sorgu türü seçimi
sorgu_turu = st.selectbox("Sorgulama Türü Seçin:", ["IP", "Domain"])

# Seçime göre giriş alanı
if sorgu_turu == "IP":
    giris = st.text_input("IP Adresi Girin:")
elif sorgu_turu == "Domain":
    giris = st.text_input("Domain Girin:")
else:
    giris = ""

# Saat aralığı seçimi
col1, col2 = st.columns(2)
with col1:
    start_time = st.time_input("Başlangıç Saati", value=time(0, 0))
with col2:
    end_time = st.time_input("Bitiş Saati", value=time(23, 59))

# Ek seçenekler
col3, col4 = st.columns(2)
with col3:
    konum_bilgisi = st.radio("Konum bilgisi ister misiniz?", ("Evet", "Hayır"), horizontal=True)
with col4:
    alt_domain_bilgisi = st.radio("Alt domain bilgisi ister misiniz?", ("Evet", "Hayır"), horizontal=True)

# Sorgula butonu
if st.button("Sorgula"):
    # Örnek veriyle simülasyon
    example_sites = [
        {"site": "blog.hilemnurerdem.com", "zaman": "10:00-11:00"},
        {"site": "forum.example.com", "zaman": "12:00-13:00"},
        {"site": "shop.hilemnurerdem.com", "zaman": "15:00-16:00"},
    ]
    example_location = {"ülke": "Türkiye", "şehir": "İstanbul"}

    if konum_bilgisi == "Evet":
        st.subheader("Konum Bilgisi")
        st.write(f"Ülke: {example_location['ülke']}, Şehir: {example_location['şehir']}")

    st.subheader("Aktif Olunan Siteler")
    for site in example_sites:
        if "hilemnurerdem.com" in site["site"]:
            st.markdown(f"**{site['site']}** (Zaman: {site['zaman']}) :red[<-- Alt domain tespit edildi!]")
        else:
            st.write(f"{site['site']} (Zaman: {site['zaman']})")

    if alt_domain_bilgisi == "Evet":
        st.subheader("Alt Domainler ve Sunucu Bilgileri")
        alt_domainler = [
            {"alt_domain": "blog.hilemnurerdem.com", "sunucu": "213.74.123.45", "cihaz": "iPhone 11"},
            {"alt_domain": "shop.hilemnurerdem.com", "sunucu": "213.74.123.46", "cihaz": "Xiaomi Redmi Note 12 Pro"},
            {"alt_domain": "api.hilemnurerdem.com", "sunucu": "213.74.123.47", "cihaz": "MacBook Air"},
        ]
        st.table(alt_domainler)
