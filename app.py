import streamlit as st
from agents import generate_campaign

# Professional Page Setup
st.set_page_config(page_title="Cyno-Flow AI", page_icon="🚀", layout="wide")

# Sidebar for Branding
with st.sidebar:
    st.title("⚙️ Engine Settings")
    st.info("Model: Gemini 1.5 Flash")
    st.markdown("---")
    st.write("Developed by: **Gowri Nandana**")

st.title("🚀 Cyno-Flow: Campaign Engine")
st.write("Turn your business idea into a full marketing strategy instantly.")

# User Input
user_input = st.text_area("Enter your product or brand description:", 
                          placeholder="e.g., A subscription box for organic tea...")

# Action Button
if st.button("🔥 Generate Full Campaign", use_container_width=True):
    if user_input:
        with st.status("🤖 AI Agents are strategizing...", expanded=True) as status:
            # Calling the brain
            result = generate_campaign(user_input)
            status.update(label="Strategy Complete!", state="complete", expanded=False)
        
        st.divider()
        
        # Check if there was an error
        if "Error:" in result:
            st.error(result)
        else:
            st.success("Campaign Ready!")
            st.markdown(result)
            
            # Professional Download Button
            st.download_button("📩 Download Strategy", result, file_name="cyno_flow_strategy.txt")
    else:
        st.warning("Please enter a description first!")
        