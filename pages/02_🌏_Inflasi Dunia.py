import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
import requests
import geopandas as gpd
import plotly
import plotly.express as px
import numpy as np
import altair as alt

st.set_page_config(
     page_title="Inflasi",
     page_icon="📈",
     layout="wide",
     initial_sidebar_state="collapsed",
 )

df_world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
df_world_inflation = pd.read_excel("world_inflation.xlsx")

world_inflation = df_world.merge(df_world_inflation, how="left", left_on=['iso_a3'], right_on=['Country Code']).set_index('Country Name')
st.subheader("Data Inflasi Dunia")
tahun = st.slider('Input Tahun', 1960, 2021, 2021)

with st.expander("Kustomisasi Warna dan Map 🎨"):
    st.markdown("---")
    pilihan_warna = st.selectbox(
     'Kustomisasi Warna Poligon 🍭',
     ("YlOrRd","YlOrBr","YlGnBu","YlGn","Reds","Purples","PuRd","PuBu","OrRd","Oranges","Greys","Greens","GnBu","BuPu","BuGn","Blues"))
    pilihan_map = st.selectbox(
     'Kustomisasi Style Map 🗺️',
     ('stamen-watercolor','open-street-map', 'white-bg', 'carto-positron', 'carto-darkmatter', 'stamen-terrain', 'stamen-toner'))



fig = px.choropleth_mapbox(world_inflation,
                           geojson=world_inflation.geometry,
                           color = tahun,
                           mapbox_style=pilihan_map,
                           zoom = 0.1,
                           color_continuous_scale = pilihan_warna,
                           locations=world_inflation.index)
st.plotly_chart(fig)
"_Sumber: https://data.worldbank.org/_"
"_Catatan: Negara yang tidak memiliki poligon berarti tidak memiliki data pada tahun tersebut_"

top_10_high = df_world_inflation[["Country Name",tahun]].sort_values(tahun, ascending = False).head(10).reset_index(drop = True)
top_10_high.index = np.arange(1, 11)

tahun_store = str(tahun)
bar_chart_high = top_10_high.sort_values([tahun],ascending=True)
bar_chart_high.columns = bar_chart_high.columns.astype(str)

"**Sepuluh Negara Teratas dengan Inflasi Tertinggi**"
topinf1, topinf2 = st.columns([2,4])
with topinf1:
    top_10_high
with topinf2:
    st.write(alt.Chart(bar_chart_high).mark_bar().encode(
        x = tahun_store,
        y = alt.Y("Country Name", sort = '-x'),
        color=alt.value('#FFDB58')))


information = st.sidebar.markdown("_This streamlit app is made by Jessica Zerlina Sarwono as a capstone project for Tetris Program Batch 2_")
