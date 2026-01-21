import streamlit as st

start = st.Page("start.py", title="start")
home = st.Page("home.py", title="Home")
modules = st.Page("modules.py", title="Manage Modules")
chatbot = st.Page("chatbot.py", title="Chat Bot")
tests = st.Page("tests.py", title="Tests")

pg = st.navigation([home, modules, chatbot, tests])

pg.run()