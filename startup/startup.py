import pandas as pd
import streamlit as st
df=pd.read_csv('startup_funding.csv')
st.sidebar.title('Startup Funding Analysis')
option=st.sidebar.selectbox('select one',['Overall Analysis','Startup','Investor'])
if option=='Overall Analysis':
    st.title('Overall Analysis')
elif option=='Startup':
    st.sidebar.selectbox('Select Startup',['Byjus','ola','Flipkart'])
else:
    st.sidebar.selectbox('Select investor',['admi 1','admi 2','admi 3'])
    print('helo')