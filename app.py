import requests
import streamlit as st
import os

def search_lyrics(banda, music):
    endpoint = f'https://api.lyrics.ovh/v1/{banda}/{music}'
    response = requests.get(endpoint)
    return response.json()['lyrics'] if response.status_code == 200 else ''
st.title('Music lyrics')
banda = st.text_input('Artist name or band name:', key = 'banda')
music = st.text_input('Music name', key='music')
search = st.button('Search')
if search:
    lyrics = search_lyrics(banda, music)
    if lyrics:
        st.success('lyrics found ')
        st.text(f'Music: {music}')
        st.text(lyrics)
    else:
        st.error('lyrics not found, try again')
    

