import streamlit as st
from utils import st_def

st.set_page_config(page_title='👋 AI',  page_icon="🚀",)
st.title('🔍 AI')
st_def.st_logo()

st.markdown("🚀) 🍨📄Rule Extraction📚: Python Libraries  Approaches📰🍨 ")
st.image("./images/zhang.gif")

pdf1 = st.file_uploader('Upload your PDF Document', type='pdf')
#-----------------------------------------------
if pdf1:
    pdfReader = PyPDF2.PdfReader(pdf1)
    st.session_state['pdfreader'] = pdfReader
    st.success(" has loaded.")
else:
    st.info("waiting for loading ...")