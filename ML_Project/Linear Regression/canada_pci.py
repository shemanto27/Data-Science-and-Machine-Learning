import streamlit as st
import numpy as np
import pandas as pd
import joblib as joblib
from sklearn.linear_model import LinearRegression

st.write('''
# Canada's Per Capita Income Prediction App
''')

#creating Side bar
st.sidebar.header("Give Your Input Data")
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"]) 

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
else:
    st.write("Waiting CSV file to be uploaded...")
    
# loading the ML model
mj = joblib.load("canada_pci.pkl")
prediction = mj.predict(df)

st.subheader("Prediction")

st.write(prediction)
