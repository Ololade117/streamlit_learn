import streamlit as st 
symptoms = st.text_input("Enter the symptoms that you have")
medical_history = st.text_input("what is your medical history")
results = f"i will research on the following {symptoms} with the following {medical_history}"
st.text(results)