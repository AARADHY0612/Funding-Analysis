import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
df=pd.read_csv('startup_clean.csv')
#st.set_page_config(layout='wide',page_title='Startup Analysis')
#data cleaning 
#df['Investors Name']=df['Investors Name'].fillna('undisclosed')

df['date']=pd.to_datetime(df['date'],errors='coerce')
df['month']=df['date'].dt.month
df['year']=df['date'].dt.year
def load_investor_details(investor):
    st.title(investor)
    last5_df=df[df['investor'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Recent investments')
    st.dataframe(last5_df)
    #biggest investments
    big_series=df[df['investor'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
    st.subheader('Biggest Investment')
    st.dataframe(big_series)
    col1,col2=st.columns(2)
    with col1:
        st.subheader('Investments')
        fig, ax =plt.subplots()
        ax.bar(big_series.index,big_series.values)
        st.pyplot(fig)


    with col2:
        st.subheader('Invested Sectors')
        vertical_series=df[df['investor'].str.contains(investor)].groupby('vertical')['amount'].sum()
        fig1,ax1=plt.subplots()
        ax1.pie(vertical_series,labels=vertical_series.index)
        st.pyplot(fig1)

    
    st.subheader('year on year investment')
    df['year']=df['date'].dt.year
    year_series=df[df['investor'].str.contains(investor)].groupby('year')['amount'].sum()
    fig2,ax2=plt.subplots()
    ax2.plot(year_series.index,year_series.values)
    st.pyplot(fig2)    

def load_overall_analysis():
    st.title('Overall Analysis')
    col1,col2,col3,col4=st.columns(4)
    with col1:
    #total invested amount 
        total=round(df['amount'].sum())
        st.metric('Total',str(total) + 'cr')
    with col2:
        #max funding
        max_funding=df.groupby('startup')['amount'].max().sort_values(ascending=False).head(1).values[0]
        st.metric('Max funding in a startup',str(max_funding) + 'cr')
    with col3:
        mean_funding=df.groupby('startup')['amount'].sum().mean()
        st.metric('Mean funding in a startup',str(round(mean_funding)) + 'cr')
    with col4:
        num_startup=df['startup'].nunique()
        st.metric('Total funded startups',num_startup)
    st.header('MoM graph')
    selected_option=st.selectbox('Select Type',['Total','Count'])
    if selected_option=='Total':
        temp_df=df.groupby(['year','month'])['amount'].sum().reset_index()
        temp_df['x']=temp_df['month'].astype(str) + '-' + temp_df['year'].astype(str)
        fig3,ax3=plt.subplots()
        ax3.plot(temp_df['x'],temp_df['amount'])
        st.pyplot(fig3)
    else:
        temp_df1=df.groupby(['year','month'])['amount'].count().reset_index()
        temp_df1['x']=temp_df1['month'].astype(str) + '-' + temp_df1['year'].astype(str)
        fig4,ax4=plt.subplots()
        ax4.plot(temp_df1['x'],temp_df1['amount'])
        st.pyplot(fig4)

        

st.sidebar.title('Startup Funding Analysis')
option=st.sidebar.selectbox('select one',['Overall Analysis','Startup','Investor'])



if option=='Overall Analysis':
   # btn3=st.sidebar.button('show overall analysis')
    #if btn3:
    load_overall_analysis()


elif option=='Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['startup'].unique().tolist()))
    st.title('Startup Analysis')
    btn1=st.sidebar.button('Find Startup Details')




else:
    selected_investor=st.sidebar.selectbox('Select investor',sorted(set(df['investor'].str.split(',').sum())))
    st.title('Investor Analysis')
    btn2=st.sidebar.button('Find Investor Details')

    if btn2:
        load_investor_details(selected_investor)

    
