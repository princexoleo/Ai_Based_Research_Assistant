import os
import re
import streamlit as st
import google.generativeai as genai
import google.ai.generativelanguage as glm
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="AI Based Research Assistant",
    page_icon=":brain:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("AI Based Research Assistant")

if __name__=="__main__":
    st.title("AI Based Research Assistant")
    st.markdown("##")
    st.write("Developed by [Mazharul Islam Leon](https://github.com/princexoleo/Ai_Based_Research_Assistant.git)")