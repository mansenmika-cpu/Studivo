import streamlit as st
import pandas as pd
import google.generativeai as genai
from style_utils import apply_custom_style

apply_custom_style()

modules_df = pd.read_csv("modules.csv")

module_list = modules_df['Modules'].tolist()

modules_list = list(set(module_list))

module = st.selectbox("📚 Module", module_list, index=None)

type = st.selectbox("Test type", ("MCQ", "Structured Essay", "Essay"))

if type == "MCQ":
    maxq = 50
else:
    maxq = 5    

num_q = st.number_input("Numebr of questions", 1, maxq)

language = st.selectbox("🌐 Choose Language", ["English", "Sinhala"], index=0)

selected_modules_df = modules_df.loc[modules_df["Modules"] == module]

selected_resources = selected_modules_df["Resources"].to_list()

system_instructions = f"""
    Imagine You have to make a test for a student.
    Student will give you the test type of type.
    Use your response language as language of {language}.
    The student will give you the module as {module}, number of questions as {num_q} and resources as {selected_resources}.
    1. Give number of questions which student need corressponding to selected resources labelly. 
    2. And give the weight of the questions out of 100.
    3. Give the instructions top.
    4. Mention the resources which you used.
    5. Give answers labelly for the questions.
    Note: Use same words in the resources when making questions.
    """

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

response = None

if st.button("Create a Test", use_container_width=True):
    model = genai.GenerativeModel(
        model_name='gemini-2.5-flash',
        system_instruction=system_instructions
    )

    with st.spinner("Creating your test..."):
        try:
            response = model.generate_content(f"Your test according to {module} module.")

            st.subheader("Your Test")
            st.markdown(f"""
                    <div style="background-color: #e8f4f8; padding: 20px; border-radius: 10px; border-left: 5px solid #2980b9;">
                        {response.text}
                    </div>
                """, unsafe_allow_html=True)
            st.session_state["student_language"] = language
            st.session_state["student_module"] = module
            st.session_state["student_number_of_questions"] = num_q
            st.session_state["student_resources"] = selected_resources

        except Exception as e:
            st.error(f"Error connecting to Gemini: {e}") 
