import streamlit as st
import requests

# Set up the Streamlit app layout
st.set_page_config(page_title="Thesis", layout="wide")

# Sidebar content
st.sidebar.title("Sidebar")
st.sidebar.write("Profile")
st.sidebar.write("Analysis")

# Main content
st.title("Technical report writing")

# Initialize session state for messages if not already initialized
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Container for the input field, button, and output
with st.container():
    # Display previous messages with styling
    for message in st.session_state.messages:
        st.markdown(
            f"""
            <div style="padding: 10px; border: 2px solid #4CAF50; border-radius: 5px; background-color: #000000; color: #FFFFFF; margin-bottom: 10px;">
                <p style="font-size: 18px; margin: 0;">{message}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Use a form for input and button alignment
    with st.form(key='bottom_form', clear_on_submit=True):
        user_input = st.text_area("Your Message:", height=40, key="input")
        submit_button = st.form_submit_button("Send")
        
        # Handle button click
        if submit_button and user_input:
            # Send user input to the Flask app
            response = requests.post('http://localhost:5000/enhance', json={'text': user_input})
            if response.status_code == 200:
                enhanced_text = response.json().get('enhanced_text', '')
                st.session_state.messages.append(f"User: {user_input}")
                st.session_state.messages.append(f"Enhanced: {enhanced_text}")
            else:
                st.error("Error in processing the text")
            
            # Refresh the page to show new message at the bottom
            st.experimental_rerun()
