import streamlit as st
import pandas as pd

st.title('my first dashboard')
st.header('I am learning streamlit')
st.subheader('and i am loving it')


st.write('hey this is a text box')

st.markdown("""
### my fav movies are 
- Race 3 
- Dhoom 3
- Bahubali
""")

st.code("""
  def square(a):
    return a**2
  
  a = square(2)
""")

df = pd.DataFrame({
  'name': ['ishan' ,'isha' , 'dhruv'],
  'mark' : [89 , 98 , 87],
  'package': [29 , 23 , 19]
})

st.dataframe(df)

st.metric('revenue' , 'Rs 3l' , '-3')

st.json({
  'name': ['ishan' ,'isha' , 'dhruv'],
  'mark' : [89 , 98 , 87],
  'package': [29 , 23 , 19]
})

# WE HAVE AUDIO, VIDEO AND IMAGES OPTION AS WELL 
# # st.audio('file name')
# # st.image('file name')
# # st.video('file name')

# creating layout 
st.sidebar.title('this is sidebar')

col1 , col2 , col3 = st.columns(3)

with col1:
  st.image('wallpaperflare.com_wallpaper (1).jpg')
with col2:
  st.image('wallpaperflare.com_wallpaper (1).jpg')
with col3:
  st.image('wallpaperflare.com_wallpaper (1).jpg')

# showing status 

st.error('login failed')
st.success('login successful')
st.info('hey this is info')
st.warning('you are doing it in wrong way')


# taking user input 
# text input -> number input -> date input

email = st.text_input('enter email')
number = st.number_input('enter the number')
st.date_input('Enter regis date')