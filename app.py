import requests
import streamlit as st
import os

def search_lyrics(banda, music):
    endpoint = f'https://api.lyrics.ovh/v1/{banda}/{music}'
    response = requests.get(endpoint)
    return response.json()['lyrics'] if response.status_code == 200 else None

def validing(question):
    if question not in ['yes', 'no']:
        return False
    return True

def new_lyrics():
    again = str(input("would you like search a new lyrics? [yes/no]: "))
    try:
        if not validing(again):
            raise ValueError
    except ValueError:
        print('only yes or no')
        new_lyrics()

    if again == 'yes':
        return True
    return False

def main():
    band = str(input('Artist name or band name: '))
    music = str(input('Music name'))
    lyrics = search_lyrics(band, music)
    if lyrics:
        print('lyrics found')
        print(f'music: {music}')
        print(lyrics)
        print('-'*100)

    else:
        print('lyrics not found')

    if new_lyrics():
        main()
    print('end')

main()


