import streamlit as st
import requests


token = st.text_input('Type in translate API token:', '')
st.write('The current token used is:', token)


url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
payload = {
	"q": "Hello, world!",
	"target": "nl",
	"source": "en"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "a8f9d97b7emshfb89cd5db62ad47p163116jsn44ffce9232ff",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}
if token != "":
	response = requests.post(url, data=payload, headers=headers)
	st.write(response.json())
