import streamlit as st
from style_utils import apply_custom_style

apply_custom_style()

st.title("🎓 STUDIVO")
st.subheader("Your Personal AI Academic Assistant")
st.divider()

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.info("Welcome back! What would you like to do today?")
    if st.button("🚀 Manage Modules", use_container_width=True):
        st.switch_page("modules.py")
        