import streamlit as st
import pandas as pd

st.set_page_config(
    page_icon=":bar_chat:",
    page_title="Dashboard Vendas Streamlit",
    layout="wide"
)

st.title('Dashboard Vendas Streamlit')
st.markdown("_Prototipo 0.1")

@st.cache_data
def load_data(file):
    data = pd.read_excel(file)
    return data

with st.sidebar:
    st.header("Configurações:")
    uploaded_file = st.file_uploader("Escolha o arquivo")

if uploaded_file is None:
    st.info(" Carregue o(s) arquivo(s) acima", icon="⚠️")
    st.stop()
    
df = load_data(uploaded_file)
with st.expander("Preview dos dados"):
    st.dataframe(
        df,
        column_config={
            "Year": st.column_config.NumberColumn(format="%d")
        }
    )