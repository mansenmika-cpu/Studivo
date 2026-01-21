import streamlit as st

def apply_custom_style():
    st.markdown("""
    <style>
        /* 1. Base App Background */
        .stApp {
            background-color: #f0f7f9; /* Extremely light blue-grey */
        }

        /* 2. Primary Headers - Deep Ocean Blue */
        h1, h2, h3 {
            color: #1e3a8a !important; /* Navy Blue */
            font-family: 'Inter', sans-serif;
            font-weight: 800;
        }

        /* 3. Cards & Forms - Green Accent */
        [data-testid="stForm"] {
            background-color: #ffffff;
            border-radius: 18px;
            border-top: 5px solid #10b981; /* Emerald Green top border */
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05);
            padding: 2rem;
            transition: transform 0.3s ease;
        }

        [data-testid="stForm"]:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 30px -10px rgba(16, 185, 129, 0.2);
        }

        /* 4. Buttons - Gradient of Blue and Green */
        .stButton > button {
            background: linear-gradient(135deg, #2563eb 0%, #10b981 100%);
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.6rem 2rem;
            font-weight: 600;
            transition: opacity 0.3s ease;
        }

        .stButton > button:hover {
            opacity: 0.9;
            color: white;
            border: none;
        }

        /* 5. Input Fields - Subtle Blue Border */
        .stTextInput input, .stSelectbox div[data-baseweb="select"], .stFileUploader section {
            border: 1px solid #bfdbfe !important; /* Soft Blue */
            border-radius: 10px !important;
        }

        /* 6. Chat Interface - Blue/Green Alternating */
        /* Assistant Message (Blue) */
        [data-testid="stChatMessage"]:nth-child(even) {
            background-color: #dbeafe !important; 
            border-left: 4px solid #2563eb;
        }
        
        /* User Message (Green) */
        [data-testid="stChatMessage"]:nth-child(odd) {
            background-color: #dcfce7 !important;
            border-left: 4px solid #10b981;
        }

        /* 7. Sidebar Customization */
        section[data-testid="stSidebar"] {
            background-color: #ffffff;
            border-right: 2px solid #e5e7eb;
        }

        /* Hide default Streamlit clutter */
        header 
        footer 

    </style>
    """, unsafe_allow_html=True)