import streamlit as st
import pandas as pd
import re
import requests

st.title('Dutch Article')
token = st.text_input('Type in translate API token:', '')

txt = st.text_area('type in the article', ' ')

path = 'data/dutch.csv'
voc = pd.read_csv(path)
add_words = []
add_translates = []


def get_translation(token, word):
	# url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    url = "https://text-translator2.p.rapidapi.com/translate"
    payload = {
		"source_language": "nl",
	    "target_language": "en",
	    "text": "sluit"
	}
    headers = {
		"content-type": "application/x-www-form-urlencoded",
		"Accept-Encoding": "application/gzip",
		"X-RapidAPI-Key": token,
		"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
	}
    response = requests.post(url, data=payload, headers=headers).json()
    st.write(response)
    new_word = response['data']['translations'][0]['translatedText']
    return new_word

def clean(word):
    pattern = r"[.,']"
    cleaned_text = re.sub(pattern, '', word.lower())
    return cleaned_text

def get_unknow_word(word, voc):
    word_ = clean(word)
    if word_ not in voc['word'].unique():
        add_words.append(word_)
        translate = get_translation(token, word)
        add_translates.append(translate)
        return f"({word}:{translate})"
    else:
        translate = voc[voc['word'] == word_]['translate'].values[0]
        return word

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

if st.button('Add all words'):
    words = txt.split()
    str_new = ' '.join(get_unknow_word(w, voc) for w in words)
    st.write(str_new)
    add_df = pd.DataFrame({'word': add_words, 'translate': add_translates})
    new_df = pd.concat([voc, add_df], axis=0)
    csv_df = convert_df(new_df)
    st.download_button(
      label="Download data as CSV",
      data=csv_df,
      file_name='dutch.csv', 
      mime='text/csv',
    )
    st.balloons()