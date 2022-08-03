import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import requests
from PIL import Image
import altair as alt
import datetime 
import numpy as np 

st.set_page_config(
     page_title="Inflasi",
     page_icon="📈",
     layout="wide",
     initial_sidebar_state="collapsed",
 )

st.title("Inflasi: _Hot Topic_ Tahun 2022?📈🤔")
st.markdown("**Journalized 3 August 2022 by Jessica Zerlina Sarwono**")
image = Image.open('inflation.jpeg')
st.image(image)
st.info('Menurut Bank Indonesia, inflasi dapat diartikan sebagai kenaikan harga barang dan jasa secara umum dan terus menerus dalam jangka waktu tertentu.')
"_\"Amerika inflasi gede ga sih? Indonesia gimana ya?\"_"
"_\"Sahamku kok fluktuasi banget ya, apa gegara inflasi ya?\"_"
"_\"Lah perasaan dulu 15rb. Kok udah 20rb aja nih jajanan?\"_"
st.markdown('<div style="text-align: justify;">Ucapan-ucapan serupa sudah tidak asing di dengar di masyarakat selama beberapa bulan terakhir. Selama beberapa tahun yang lalu, saya hanya dapat mendengar kata \"inflasi\" di buku paket ekonomi saya. Namun, akhir-akhir ini saya dan orang-orang di sekitar saya mulai sadar dengan keberadaan inflasi yang terjadi di masyarakat. Sesungguhnya, apa yang terjadi di dunia ini? Mari kita simak terlebih dahulu mengenai inflasi di negara maju dunia.</div>', unsafe_allow_html=True)
" "
st.markdown("**Kenaikan Customer Price Index (CPI) di Amerika Serikat 10 Tahun Terakhir**")
us_cpi = pd.read_excel("US CPI.xlsx")
us_cpi_data = us_cpi[["Periode","CPI"]].set_index("Periode")
st.line_chart(us_cpi_data)
"_Sumber: https://data.bls.gov/_"
st.markdown('<div style="text-align: justify;">Dapat dilihat bahwa semenjak pertengahan tahun 2021, CPI telah naik secara pesat dan memuncak pada bulan Maret 2022. Pasalnya, kenaikan CPI Amerika Serikat merefleksikan harga yang meningkat pada komoditas yang ada, sekaligus mencerminkan inflasi. Untuk menangani CPI yang tinggi, bank sentral Amerika Serikat atau The Fed akan terdorong untuk menaikkan suku bunga. Kenaikan dari suku bunga dolar Amerika Serikat yang merupakan mata uang dunia merupakan hal yang harus diwaspadai oleh negara-negara di dunia. Hal ini disebabkan karena fluktuasi suku bunga tersebut akan mengakibatkan menguat atau melemahnya mata uang di seluruh dunia.</div>', unsafe_allow_html=True)
" "

st.markdown("**Inflasi di Inggris**")
st.markdown('<div style="text-align: justify;">Tidak hanya di Amerika Serikat, tetapi inflasi rupanya juga menjadi salah satu topik hangat di Inggris. Salah satu tweet berisi berita yang dilansir oleh @cnbcindonesia menunjukkan bahwa harga burger McDonalds mengalami kenaikan sebesar 20%. Kenaikan ini merupakan salah satu kenaikan yang menghebohkan publik dikarenakan burger McDonalds tersebut mengalami kenaikan harga setelah berada pada harga yang sama selama 14 tahun.</div>', unsafe_allow_html=True)
" "

class Tweet(object):
    def __init__(self, s, embed_str=False):
        if not embed_str:
            # Use Twitter's oEmbed API
            # https://dev.twitter.com/web/embedded-tweets
            api = "https://publish.twitter.com/oembed?url={}".format(s)
            response = requests.get(api)
            self.text = response.json()["html"]
        else:
            self.text = s

    def _repr_html_(self):
        return self.text

    def component(self):
        return components.html(self.text, height=700)


t1 = Tweet("https://twitter.com/cnbcindonesia/status/1552551427796799488").component()


st.markdown("**Lantas, bagaimana kondisi inflasi di Indonesia?**")

data = pd.read_excel("Data Inflasi.xlsx")
count_inflasi = pd.read_excel("inflasi_count.xlsx")

data['Periode'] = pd.to_datetime(data['Periode'])
data['Inflasi'] = data['Inflasi'].replace(',','.',regex=True).astype(float)
inflasi_indo = data[['Periode','Inflasi']].set_index('Periode')
st.line_chart(inflasi_indo)
"_Sumber: https://www.bi.go.id/_"
st.markdown('<div style="text-align: justify;">Tren inflasi di Indonesia tidak menunjukkan kenaikan sepesat Amerika Serikat. Namun, dapat dilihat bahwa pada tahun 2022, Indonesia mulai mengalami kenaikan pada inflasi. Saya ingin mengetahui lebih lanjut, kira-kira apakah warganet benar-benar merasakan dampak dari inflasi ini? Atau hanya orang-orang di sekitar saya saja yang membicarakan tentang inflasi? Untuk mengetahui hal ini, saya melakukan scraping terhadap counts twitter untuk memahami seberapa sering warganet membicarakan terkait inflasi.</div>', unsafe_allow_html=True)
" "


count_inflasi['tanggal'] = count_inflasi['tanggal'].astype(str)
scatter  = alt.Chart(count_inflasi).mark_point(filled=True).encode(
        alt.X('tanggal', title = "Tanggal"),
        alt.Y('jumlah tweet', title = "Jumlah Tweet"),
        alt.OpacityValue(1)).interactive().properties(
    width=800,
    height=300
)

count_inflasi.index = np.arange(1, 7)
count1,count2 = st.columns([2,4])
with count1:
    count_inflasi
with count2:
    st.altair_chart(scatter)




"_Data diambil pada hari Rabu, 3 Agustus 2022 pukul 22:15_"

st.markdown('<div style="text-align: justify;">Ternyata, meskipun inflasi di Indonesia tidak menunjukkan tren yang separah di Amerika, dapat dilihat bahwa warganet di Indonesia juga merasakan keberadaan inflasi. Hal ini dicerminkan dari kata inflasi yang masih tergolong sangat sering disebut dalam tweets dengan satuan ribuan setiap harinya selama beberapa hari terakhir dan melonjak hingga di atas 12000 pada tanggal 29 Juli 2022. Adapun salah satu postingan yang menarik perhatian publik dan diduga menjadi penyebab lonjakan ini dipublish oleh akun dengan username @Istyanyan yang menunjukkan berbandingan antara ukuran jajanan momogi yang lama dengan yang baru. Ternyata, warganet banyak yang merasakan inflasi di Indonesia melalui perubahan ukuran cemilan sejuta umat ini 🤣.</div>', unsafe_allow_html=True)

t = Tweet("https://twitter.com/Istyanyan/status/1552636051440963585/").component()

st.markdown("---")
"Untuk mengetahui lebih lanjut mengenai inflasi Indonesia di bulan Juli, pergilah ke halaman 🔴 Inflasi Indonesia"
"Untuk mengetahui lebih lanjut mengenai inflasi di dunia hingga 2021, pergilah ke halaman 🌏 Inflasi Dunia"
information = st.sidebar.markdown("_This streamlit app is made by Jessica Zerlina Sarwono as a capstone project for Tetris Program Batch 2_")

