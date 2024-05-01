import streamlit as st
from utils import st_def

st.set_page_config(page_title='👋 AI',  page_icon="🚀",)
st.title('🔍 AI')
st_def.st_logo()
#------------------------------------------------------------------------------------------------
tab1, tab2 = st.tabs(["Upload Receipt", "Display the Data"])
with tab1:
    st.markdown('An electronic receipt, commonly known as an e-receipt, is a digital version of a traditional paper receipt that is generated and delivered electronically. Instead of a tangible piece of paper, e-receipts are sent via electronic channels, such as email or mobile applications, as proof of a transaction. They include the same transaction information as paper receipts, such as the date, time, and items purchased.')
  

with tab2:
        st.warning("Please upload a PDF to display the data.")
    