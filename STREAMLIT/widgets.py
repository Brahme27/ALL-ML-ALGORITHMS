import streamlit as st

st.title('STREAMLIT TEXT INPUT')

name=st.text_input("Enter your name:")

if name:
    st.write(f"Bane set iyndi ra pilla {name}")