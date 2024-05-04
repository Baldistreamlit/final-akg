import streamlit as st
import pandas as pd

def hitung_kecukupan_gizi_umur_berat_badan_tinggi_umum(umur, berat_badan, tinggi, jenis_kelamin):
    # Hitung kebutuhan energi dasar (Basal Metabolic Rate/BMR) berdasarkan rumus Harris-Benedict
    if jenis_kelamin.lower() == 'laki-laki':
        bmr = 88.362 + (13.397 * berat_badan) + (4.799 * tinggi) - (5.677 * umur)
    elif jenis_kelamin.lower() == 'perempuan':
        bmr = 447.593 + (9.247 * berat_badan) + (3.098 * tinggi) - (4.330 * umur)
    else:
        return "Jenis kelamin tidak valid"

    # Hitung Total Energy Expenditure (TEE) berdasarkan aktivitas fisik
    # Misalnya, menggunakan faktor aktivitas fisik sedentary (1.2)
    faktor_aktivitas = 1.2
    tee = bmr * faktor_aktivitas

    # Hitung kebutuhan energi total (Total Daily Energy Expenditure/TDEE) perhari
    tdee = tee

    return tdee

def main():
    # CSS untuk mengatur font menjadi Times New Roman
    st.write(
        """
        <style>
        body {
            font-family: "Times New Roman", Times, serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('Kalkulator Kecukupan Gizi')

    # Judul sebelum kalkulator
    st.write('<div class="red-divider"></div>', unsafe_allow_html=True)
    st.markdown(
        """<style>
        .red-divider {
            color: red;
            border-bottom: 3px solid red;
            border-radius: 2px;
            padding: 2px;
            margin-bottom: 20px;
        }
        </style>""",
        unsafe_allow_html=True
    )

    st.write("### Penjelasan Sebelum Kalkulator")
    st.write("Selamat datang di Kalkulator Kecukupan Gizi! Aplikasi ini dapat membantu Anda menghitung kebutuhan energi harian berdasarkan umur, berat badan, tinggi, jenis kelamin, dan tingkat aktivitas fisik. "
             "Silakan isi informasi Anda di bawah ini dan tekan tombol 'Hitung' untuk melihat hasilnya.")
    st.write('<div class="red-divider"></div>', unsafe_allow_html=True)

    umur = st.number_input('Masukkan umur (tahun)', min_value=0, step=1)
    berat_badan = st.number_input('Masukkan berat badan (kg)', min_value=0.0, step=0.1)
    tinggi = st.number_input('Masukkan tinggi (cm)', min_value=0.0, step=0.1)
    jenis_kelamin = st.selectbox('Pilih jenis kelamin', ['Laki-laki', 'Perempuan'])

    # Pembatas dengan warna merah
    st.write("---")
    st.markdown(
        """<style>
        .red-divider {
            color: red;
            border-bottom: 3px solid red;
            border-radius: 2px;
            padding: 2px;
            margin: 10px 0;
        }
        </style>""",
        unsafe_allow_html=True
    )
    st.write('<div class="red-divider"></div>', unsafe_allow_html=True)

    # Informasi nama anggota kelompok dan tim
    st.sidebar.title('Informasi Tim')
    st.sidebar.write('Kelompok 4')
    st.sidebar.write('Anggota:')
    st.sidebar.write('- Amara Rifa Pratamy')
    st.sidebar.write('- Muhammad Baldiyansyah')
    st.sidebar.write('- Shofi Nabila Khoirunnisa')
    st.sidebar.write('- Tabitha Zoeana Salsabila')
    st.sidebar.write('- Afdatul Saputra')

    # Tabel informasi kalori makanan
    st.write("---")
    st.write("### Tabel Informasi Kalori Makanan:")
    kalori_makanan = pd.DataFrame({
        "Makanan": ["Apel", "Pisang", "Ayam goreng", "Roti gandum", "Telur rebus", "Salmon panggang", "Nasi putih", "Kentang rebus", "Brokoli", "Yogurt rendah lemak",
                    "Kacang almond", "Tomat", "Oatmeal", "Bayam", "Wortel", "Mangga", "Beras coklat", "Roti putih", "Daging sapi panggang", "Keju cheddar",
                    "Kacang kedelai", "Jeruk", "Quinoa", "Lobak", "Ikan tuna kalengan dalam air", "Kacang polong", "Susu rendah lemak", "Mentimun", "Dada ayam tanpa kulit panggang",
                    "Anggur", "Telur orak-arik", "Kacang merah", "Labu", "Roti gandum utuh panggang", "Bayam", "Brokoli", "Jagung manis", "Buncis", "Nanas",
                    "Seledri", "Kembang kol", "Pepaya", "Paprika merah", "Bawang bombay", "Aprikot", "Kiwi", "Labu kuning", "Labu air", "Semangka", "Salak"],
        "Kalori": ["95 kalori", "105 kalori", "220 kalori", "70 kalori", "70 kalori", "206 kalori", "200 kalori", "110 kalori", "50 kalori", "120 kalori",
                   "160 kalori", "25 kalori", "150 kalori", "7 kalori", "25 kalori", "135 kalori", "216 kalori", "80 kalori", "250 kalori", "110 kalori",
                   "127 kalori", "62 kalori", "222 kalori", "45 kalori", "130 kalori", "67 kalori", "90 kalori", "16 kalori", "165 kalori", "104 kalori",
                   "140 kalori", "110 kalori", "30 kalori", "80 kalori", "7 kalori", "55 kalori", "130 kalori", "31 kalori", "82 kalori", "6 kalori",
                   "25 kalori", "59 kalori", "37 kalori", "44 kalori", "17 kalori", "42 kalori", "50 kalori", "30 kalori", "86 kalori", "82 kalori"]
    })
    st.dataframe(kalori_makanan)

    # Pembatas dengan warna merah
    st.write("---")
    st.markdown(
        """<style>
        .red-divider {
            color: red;
            border-bottom: 3px solid red;
            border-radius: 2px;
            padding: 2px;
            margin: 10px 0;
        }
        </style>""",
        unsafe_allow_html=True
    )
    st.write('<div class="red-divider"></div>', unsafe_allow_html=True)

    asupan_kalori = st.text_input('Masukkan jumlah kalori yang Anda konsumsi hari ini (masukan 0 bila tidak ingin memasukan)')

    if st.button('Hitung'):
        if asupan_kalori:
            asupan_kalori = float(asupan_kalori)
            kecukupan_gizi = hitung_kecukupan_gizi_umur_berat_badan_tinggi_umum(umur, berat_badan, tinggi, jenis_kelamin)
            st.write("Angka Kecukupan Gizi perhari:", kecukupan_gizi, "kcal")

            # Membandingkan asupan kalori dengan kebutuhan kalori harian
            if asupan_kalori < kecukupan_gizi:
                st.write("Asupan kalori Anda kurang dari kebutuhan harian Anda. Pastikan untuk mengonsumsi makanan yang cukup untuk memenuhi kebutuhan gizi Anda.")
                st.write("Disarankan untuk menambahkan makanan bergizi seperti buah, sayuran, protein, dan karbohidrat kompleks.")
            elif asupan_kalori > kecukupan_gizi:
                st.write("Asupan kalori Anda melebihi kebutuhan harian Anda. Pastikan untuk mengonsumsi makanan dengan bijak dan sesuai dengan kebutuhan gizi Anda.")
                st.write("Disarankan untuk mengurangi konsumsi makanan tinggi lemak jenuh, gula tambahan, dan garam.")
            else:
                st.write("Asupan kalori Anda telah mencukupi kebutuhan harian Anda. Pertahankan pola makan yang seimbang untuk menjaga kesehatan Anda.")
        else:
            st.write("Anda belum memasukkan jumlah kalori yang Anda konsumsi. Silakan masukkan jumlah kalori atau biarkan kosong jika tidak ingin memasukkan.")

        # Pembatas dengan warna merah
        st.write("---")
        st.markdown(
            """<style>
            .red-divider {
                color: red;
                border-bottom: 3px solid red;
                border-radius: 2px;
                padding: 2px;
                margin: 10px 0;
            }
            </style>""",
            unsafe_allow_html=True
        )
        st.write('<div class="red-divider"></div>', unsafe_allow_html=True)

        # Informasi tips untuk menjaga kalori agar sesuai dengan kebutuhan
        st.write("### Tips Menjaga Kalori Sesuai dengan Kebutuhan:")
        st.write("1. Pilih makanan yang kaya akan nutrisi seperti buah-buahan, sayuran, biji-bijian utuh, dan protein tanpa lemak.")
        st.write("2. Kurangi konsumsi makanan dan minuman tinggi gula tambahan, lemak jenuh, dan garam.")
        st.write("3. Perhatikan porsi makanan Anda dan hindari makan berlebihan.")
        st.write("4. Perbanyak aktivitas fisik dengan berolahraga secara teratur.")
        st.write("5. Minumlah cukup air setiap hari untuk menjaga hidrasi tubuh.")

if __name__ == "__main__":
    main()
