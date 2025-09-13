import streamlit as st
import pandas as pd

st.title("Data Viewer")

uploaded_file = st.file_uploader("Upload a CSV")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Data:")
    st.dataframe(df)
