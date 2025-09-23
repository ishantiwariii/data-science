import streamlit as st
import pandas as pd

df = pd.read_csv(r'D:\practice languages\python\ds cx\streamlit\startup_funding.csv')

# data cleaning
df['Investorsxe2x80x99 Name']=df['Investorsxe2x80x99 Name'].fillna('Not Disclosed')

st.sidebar.title('Startup Funding Analyser')
option = st.sidebar.selectbox('Select one' ,['Overall Analysis' , 'Startup' , 'Investor'])

if option == "Overall Analysis":
  st.title('Overall Analysis')

elif option == "Startup":
  st.sidebar.selectbox('Select Startup', sorted(df['Startup Name'].unique().tolist()))
  btn1 = st.sidebar.button('Find Startup Details')
  st.title('Startup Analysis')

else :
  st.sidebar.selectbox('Select investor', sorted(df['Investorsxe2x80x99 Name'].unique().tolist()))
  btn2 = st.sidebar.button('Find investor Details')
  st.title('Investor Analysis')

