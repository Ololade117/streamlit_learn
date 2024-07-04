def hello():
    return "Hello World"
hello()
import streamlit as st
st.text("Hello")
st.date_input('Date input')
#from hello_world import FOO
#print(FOO)
#input("Name")
Age = st.text_input("Age")
print(Age)
st.text(Age)