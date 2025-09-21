import streamlit as st

email = st.text_input('enter the input')
password = st.text_input('enter the password')
gender = st.selectbox('select gender' , ['male' , 'female' , 'other'])
btn = st.button('login kro')

if btn:
  if email == 'ishantiwari@gmail.com' and password == 'ishan':
    st.write(gender)
    st.balloons()
  else:
    st.error('login unsuccessful')