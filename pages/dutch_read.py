import streamlit as st
import requests
import pandas as pd





article = """
Woningcorporatie Vesteda verbreekt het contact met kandidaat-huurders die de organisatie willen omkopen om zo een huurwoning te bemachtigen. De potentiële huurders bieden steeds vaker geld om voorrang te krijgen op een woning.

Vesteda verhuurt appartementen en andere woningen in heel Nederland. De krappe verhuurmarkt leidt volgens Vesteda tot ongewenst gedrag zoals pogingen tot omkoping. Het gaat om bedragen die oplopen tot 5000 euro.
"""



df = pd.read_csv('https://raw.githubusercontent.com/cheerzhang/common_tool/main/data/dutch.csv')
df = df [['word','translate']]

# -----------------------  logic --------------------------- #
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
arr_known_word = df['word'].unique()
words_list = []
for i in words:
	if i not in arr_known_word:
		words_list.append(i.lower().strip('.'))

options = st.multiselect('Choose words to translate', words_list, [])
word_ = ' '.join(options)
word_meaning = ''
df_word_arr = []
df_translate_arr = []

if st.button('Translate this word'):
    # search on dict first
    if word_ in arr_known_word:
	    word_meaning = 'you should know it'
    else:
	    word_meaning = 'translated'
	    arr_known_word = arr_known_word + [word_]
	    df_word_arr.append(word_)
	    df_translate_arr.append(word_meaning)
    st.write(f'Word: {word_} means {word_meaning}')
    
new_df = pd.DataFrame({
	'word': df_word_arr,
	'translate': df_translate_arr
})
st.dataframe(new_df)
comfbine_df = pd.concat([df, new_df], axis=0)

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(comfbine_df)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='dutch.csv', 
    mime='text/csv',
)
