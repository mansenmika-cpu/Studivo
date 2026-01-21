import streamlit as st
import pandas as pd
import os
from style_utils import apply_custom_style

apply_custom_style()

st.title("🛠 Module Management")

with st.form(key='add_module', clear_on_submit=True):
    st.write("### ✨ Add New Module")
    module_name = st.text_input("Module Name", placeholder="Eneter a module name...")
    resources = st.file_uploader("Upload Study Material", type=['pdf', 'docx', 'txt', 'csv'], accept_multiple_files=True)
    submit = st.form_submit_button(label='ADD MODULE')

if submit and module_name:
    new_data = pd.DataFrame({"Modules": [module_name], "Resources": [str(resources)]})
    header_needed = not os.path.exists("modules.csv")
    new_data.to_csv("modules.csv", mode='a', index=False, header=header_needed)
    st.success(f"Add to {module_name} module!")

modules_df = pd.read_csv("modules.csv")

module_list = modules_df['Modules'].tolist()

modules_list = list(set(module_list))

with st.form(key='delete_module'):
    st.write("### 🗑️ Delete Modules")
    del_module = st.selectbox(
    "Module",
    module_list,
    index=None,
    placeholder="Select a module to delete...",
    )
    submit1 = st.form_submit_button(label='DELETE')

if submit1:
    modules_df = modules_df[modules_df['Modules'] != del_module]  
    modules_df.to_csv("modules.csv", index=False)
    st.success(f"Deleted {del_module} module!")  


