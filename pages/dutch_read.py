import streamlit as st
import requests
from data.vocabulary import arr_stop_word, arr_known_word




article = """
Woningcorporatie Vesteda verbreekt het contact met kandidaat-huurders die de organisatie willen omkopen om zo een huurwoning te bemachtigen. De potentiële huurders bieden steeds vaker geld om voorrang te krijgen op een woning.

Vesteda verhuurt appartementen en andere woningen in heel Nederland. De krappe verhuurmarkt leidt volgens Vesteda tot ongewenst gedrag zoals pogingen tot omkoping. Het gaat om bedragen die oplopen tot 5000 euro.
"""



token = st.text_input('Type in translate API token:', '')
st.write('The current token used is:', token)
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
	# st.write(response)
	new_word = response['data']['translations'][0]['translatedText']
	return new_word

st.markdown(article)
words = list(set(article.split()))
except_arr = arr_stop_word + arr_known_word
words_list = []
for i in words:
	if i not in except_arr:
		words_list.append(i.lower().strip('.'))

options = st.multiselect('Chose words to translate', words_list, [])


if st.button('Translate this word'):
	if token != "" and options != "":
		# word_meaning = get_translation(token, options)
		word_meaning = 'translated'
		st.write(f'words:{options} means {word_meaning}')

data = {word: word_meaning}
st.write(data)
if st.button('Save this word'):
	st.write(f'Ok, no problem, save {word} with {word_meaning}')

