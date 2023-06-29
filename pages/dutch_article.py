import streamlit as st
import requests

url = "https://text-translator2.p.rapidapi.com/translate"

payload = {
	"source_language": "en",
	"target_language": "id",
	"text": "What is your name?"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())
