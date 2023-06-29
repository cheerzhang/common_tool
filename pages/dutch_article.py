import streamlit as st
import requests


title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

url = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

'''
payload = { "q": "English is hard, but detectably so" }
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": token,
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())
'''
