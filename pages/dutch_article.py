import streamlit as st
import requests


def get_translation(token, word):
	url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
	payload = {
		"q": word,
		"target": "zh-cn",
		"source": "nl"
	}
	headers = {
		"content-type": "application/x-www-form-urlencoded",
		"Accept-Encoding": "application/gzip",
		"X-RapidAPI-Key": token,
		"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
	}
	response = requests.post(url, data=payload, headers=headers).json()
	st.write(response)
    return response['data']['translations'][0]['translatedText']

token = st.text_input('Type in translate API token:', '')
st.write('The current token used is:', token)



if token != "":
	word_meaning = get_translation(token, word)
	st.write(word_meaning)
