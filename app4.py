import streamlit as st
from newsapi import NewsApiClient
from msapi import apikey
newsapi = NewsApiClient(api_key=apikey)

def app():
    st.header('Top Headlines in Science')
    if st.button('Get News'):
        top_headlines = newsapi.get_top_headlines(country='in',category='science')
        st.write(top_headlines)

