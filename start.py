import streamlit as st

start = st.Page("start.py", title="Start", icon=":material/play_circle:")
home = st.Page("home.py", title="Home", icon=":material/home:")
modules = st.Page("modules.py", title="Manage Modules", icon=":material/library_books:")
chatbot = st.Page("chatbot.py", title="Chat Bot", icon=":material/smart_toy:")
tests = st.Page("tests.py", title="Tests", icon=":material/quiz:")

pg = st.navigation([home, modules, chatbot, tests])

pg.run()
