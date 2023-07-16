import streamlit as st, secrets
import pandas as pd
import re, os, requests

st.title('Dutch Article')

if 'translate_api_token' not in st.session_state:
    token = st.text_input('Type in translate API token:', '')
    # secrets.set("translate_api_token", token) 
    st.session_state['translate_api_token'] = token
else:
    # token = secrets["translate_api_token"]
    token = st.session_state['translate_api_token']

txt = st.text_area('type in the article', ' ')

path = 'data/dutch.csv'
voc = pd.read_csv(path)

if 'add_words' not in st.session_state:
    st.session_state['add_words'] = []
if 'add_translates' not in st.session_state:
    st.session_state['add_translates'] = []


def get_translation(token, word):
	# url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
    url = "https://text-translator2.p.rapidapi.com/translate"
    payload = {
		"source_language": "nl",
	    "target_language": "en",
	    "text": word
	}
    headers = {
		"content-type": "application/x-www-form-urlencoded",
		"Accept-Encoding": "application/gzip",
		"X-RapidAPI-Key": token,
		"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
	}
    new_word = ''
    response = requests.post(url, data=payload, headers=headers).json()
    if response['status'] == 'success':
        new_word = response['data']['translatedText']
        return new_word
    else:
        st.write(response)
        return new_word

def clean(word):
    pattern = r"[.,']"
    cleaned_text = re.sub(pattern, '', word.lower())
    return cleaned_text

def get_unknow_word(word, voc):
    word_ = clean(word)
    if word_ not in voc['word'].unique():
        st.session_state['add_words'].append(word_)
        translate = get_translation(st.session_state['translate_api_token'], word).strip('\n')
        st.session_state['add_translates'].append(translate)
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
    add_df = pd.DataFrame({'word': st.session_state['add_words'], 'translate': st.session_state['add_translates']})
    check_new = pd.concat([voc, add_df], axis=0)
    str_new = ' '.join(get_unknow_word(w, voc) for w in words)
    st.write(str_new)
    add_df = pd.DataFrame({'word': st.session_state['add_words'], 'translate': st.session_state['add_translates']})
    new_df = pd.concat([voc, add_df], axis=0)
    csv_df = convert_df(new_df)
    st.download_button(
      label="Download data as CSV",
      data=csv_df,
      file_name='dutch.csv', 
      mime='text/csv',
    )
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'dutch.csv')
    new_df.to_csv(file_path, index=False)
    st.balloons()