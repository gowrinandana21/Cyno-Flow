import streamlit as st
import time
from agents import improve_text # This imports your "brain"

st.set_page_config(page_title="Cyno-Flow", layout="wide")

st.header("Cyno-Flow: Campaign Engine")

# 1. User Input
user_input = st.text_area("What is your draft campaign message?", "Buy our cool new shoes!")

col1, col2 = st.columns(2)

# 2. The Logic
if st.button("Generate Coordinated Campaign"):
    with st.status("AI is thinking...") as status:
        st.write("Analyzing tone...")
        time.sleep(1)
        
        # This is where the magic happens!
        result = improve_text(user_input)
        
        status.update(label="Campaign Ready!", state="complete")

    with col1:
        st.subheader("Original Input")
        st.info(user_input)

    with col2:
        st.subheader("AI Generated Content")
        st.success(result)