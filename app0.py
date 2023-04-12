import streamlit as st
from newsapi import NewsApiClient
from msapi import apikey
newsapi = NewsApiClient(api_key=apikey)

def app():
    st.header('Top Headlines')
    if st.button('Get News'):
        top_headlines = newsapi.get_top_headlines(category='general',country='in')
        st.write(top_headlines)

