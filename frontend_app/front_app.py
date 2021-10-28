import requests
import streamlit as st
import json as js

st.title("Sentiment Analysis App")
form = st.form(key='Sentiment App')
input_text = form.text_input(label='Input Text')
submit_button = form.form_submit_button(label='Submit')

if submit_button:
    res = requests.post("http://localhost:8080/sentiment", data=js.dumps({"input_text": input_text}))
    st.success(res.text)
