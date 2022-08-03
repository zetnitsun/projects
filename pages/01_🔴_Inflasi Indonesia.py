import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import requests
import geopandas as gpd
import plotly
import plotly.express as px
import numpy as np

st.set_page_config(
     page_title="Inflasi",
     page_icon="📈",
     layout="wide",
     initial_sidebar_state="collapsed",
 )

st.subheader("Lebih Lanjut: Kondisi Inflasi Indonesia pada Juli 2022?")

met1, met2, met3 = st.columns(3)

with met1:
    st.metric(label="Inflasi Inti (mtm)", value="0.28%", delta="0.09%")
with met2:
    st.metric(label="Inflasi Volatile Foods (mtm)", value="1.41%", delta="-1.1%")
with met3:
    st.metric(label="Inflasi Administered Prices (mtm)", value="1.17%", delta="0.9%")
"_Catatan: kenaikan dan penurunan dibandingkan dengan data pada Juni 2022_"

data = pd.read_excel("Data Inflasi.xlsx")

data['Periode'] = pd.to_datetime(data['Periode'])
data['Inflasi'] = data['Inflasi'].replace(',','.',regex=True).astype(float)
inflasi_indo = data[['Periode','Inflasi']].set_index('Periode')
st.line_chart(inflasi_indo)

"_Sumber: https://www.bi.go.id/_"


st.markdown('<div style="text-align: justify;">Pada bulan Juli 2022, dapat dilihat bahwa inflasi di Indonesia secara umum telah meningkat hingga angka 4,94% (yoy). Hal ini berarti bahwa inflasi di Indonesia telah mencapai titik tertinggi sejak Oktober 2015. Meskipun terjadi kenaikan, lonjakan inflasi masih tergolong naik secara stabil dan terkontrol. Inflasi inti, volatile foods, dan administred prices masih tergolong aman dan terkendali. Lantas, bagaimana kabar dari IHSG dan perkembangannya di dalam inflasi yang kian memuncak ini? Apakah ada hubungan antara inflasi dengan IHSG yang sekiranya membuat para trader pasar modal panik akhir-akhir ini? Mari kita simak lebih lanjut!</div>', unsafe_allow_html=True)

stock = pd.read_excel("IHSG.xlsx")
stock['Periode'] = pd.to_datetime(stock['Periode'])
stock['Persen Perubahan pada IHSG'] = stock['Persen Perbuahan pada IHSG'].replace(',','.',regex=True).astype(float)

indo_data = pd.DataFrame()
indo_data["Periode"] = data["Periode"]
indo_data["Inflasi"] = data["Inflasi"]
indo_data["Persen Perubahan pada IHSG"] = stock["Persen Perubahan pada IHSG"]
indo_data = indo_data[['Periode','Inflasi','Persen Perubahan pada IHSG']].set_index('Periode')
if st.button('Kilk untuk Mengetahui Hubungan Inflasi dengan IHSG'):
     corr = np.corrcoef(indo_data['Inflasi'],indo_data['Persen Perubahan pada IHSG'])
     st.line_chart(indo_data)
     "_Sumber: https://www.bi.go.id/ dan https://www.investing.com/_"
     st.write("Koefisien korelasi spearman: ",corr[0,1])
     st.markdown('<div style="text-align: justify;">Ternyata, didapat bahwa korelasi antara inflasi di Indonesia dengan IHSG bulanan mendekati 0 atau nyaris tidak ada korelasi. Hal ini berarti bahwa nilai dari IHSG ternyata tidak akan semata-mata terpengaruh oleh inflasi secara umum, tetapi analisis perlu dilakukan lebih lanjut pada komoditas masing-masing pada pasar modal. Oleh karena itu, apabila Anda merupakan trader dalam pasar modal, alangkah baiknya menganalisis lebih lanjut mengenai saham dari komoditas dalam pasar modal dan tidak panik terlebih dahulu ketika melihat kondisi inflasi yang ada dalam masyarakat.</div>', unsafe_allow_html=True)


information = st.sidebar.markdown("_This streamlit app is made by Jessica Zerlina Sarwono as a capstone project for Tetris Program Batch 2_")
