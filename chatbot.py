import streamlit as st
import pandas as pd
import google.generativeai as genai
from PIL import Image
from style_utils import apply_custom_style

apply_custom_style()

modules_df = pd.read_csv("modules.csv")

module_list = modules_df['Modules'].tolist()

modules_list = list(set(module_list))

st.title("🤖 Studivo Tutor")

col1, col2 = st.columns(2)
with col1:
    module = st.selectbox("📚 Select Module", module_list, index=None)
with col2:
    language = st.selectbox("🌐 Choose Language", ["English", "Sinhala"], index=0)

st.divider()

selected_modules_df = modules_df.loc[modules_df["Modules"] == module]

selected_resources = selected_modules_df["Resources"].to_list()

files = st.file_uploader("Upload files", type=["png", "jpg", "jpeg",'pdf', 'docx', 'txt', 'csv'], accept_multiple_files=True)


system_instruction = f"""
    Imagine you are a tutor for solving student's academic questions.
    The student will give you module name of {module}, resources of {selected_resources}, language of {language} to give the response and files of {files}.
    If student did not give a language use English as language and if student did not give files then ignore files.
    1. Analyze the question by using module name ,resources, files (if given) from asking language.
    2. Give the answer for the question step by step.
    3. Recheck your answer.
    4. Give the brief final answer acording to the module and resources.
    """

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel(
        model_name='gemini-3-flash-preview',
        system_instruction=system_instruction
    )

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask about your notes or images..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            # Create the multimodal payload
            content_to_send = [prompt]
            
            # Check if images were uploaded in the file_uploader
            if files:
                for file in files:
                    if file.type in ["image/png", "image/jpeg", "image/jpg"]:
                        img = Image.open(file)
                        content_to_send.append(img)

            # Generate response using the content list
            response = model.generate_content(content_to_send)
            
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            
        except Exception as e:
            st.error(f"Error: {e}")


