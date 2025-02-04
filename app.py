import streamlit as st#to run the file use [streamlit run file_name.py]
import pandas as pd
st.title('startup dashboard')#title of the page 
st.header('I am learning streamlit')
st.subheader('and loving it ')
st.write('this is a normal text ')

st.markdown("""
### My favorite movies    
 - race 3
 - tiger
""")
st.code("""
print("hello world ")
""")

st.latex('x^2+y^2+2=0')

df=pd.DataFrame({
    'name':['nitish','ankit','anupam'],
    'marks':[50,60,70],
    'package':[10,12,13]
})
st.dataframe(df)
st.metric('revenue','6L','+10%')
st.json({
    'name':['nitish','ankit','anupam'],
    'marks':[50,60,70],
    'package':[10,12,13]
})
st.sidebar.title('sidebar ka tile')
col1,col2=st.columns(2)
with col1:
    st.image('output.png')
with col2:
    st.image('output.png')