import app0
import app1 
import app2
import app3
import app4
import app5
import app6
import app7

import streamlit as st

st.title('Personalised News Feed using AWS')
PAGES = {
    "General": app0,
    "Business": app1,
    "Entertainment": app2,
    "Health": app3,
    "Science": app4,
    "Sports": app5,
    "Technology": app6,
    "Global News": app7
}
st.sidebar.title('Dashboard')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()