import streamlit as st
import sys
import os

# Add the parent directory to the path so we can import from app
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from app.rag_pipeline import get_medical_response
from app.chat_history import ChatHistory
from app.ui_components import load_custom_css, render_chat_history, render_initial_message

# Page configuration
st.set_page_config(
    page_title="AI Medical Assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_custom_css()

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = ChatHistory()
    st.session_state.show_welcome = True

# Function to handle user messages
def handle_user_message():
    user_message = st.session_state.user_input
    
    if user_message.strip():
        # Add user message to chat history
        st.session_state.chat_history.add_user_message(user_message)
        
        # Clear the input box
        st.session_state.user_input = ""
        
        # Add user context from sidebar if available
        context = ""
        if st.session_state.get('age', 0) > 0:
            context += f"Age: {st.session_state.age}. "
        if st.session_state.get('gender', ''):
            context += f"Gender: {st.session_state.gender}. "
        if st.session_state.get('medical_history', []) and "None" not in st.session_state.medical_history:
            context += f"Medical history: {', '.join(st.session_state.medical_history)}. "
        if st.session_state.get('medications', ''):
            context += f"Current medications: {st.session_state.medications}."
            
        # Combine user message with context if available
        query = user_message
        if context:
            query += f"\n\nAdditional context: {context}"
            
        # Get formatted chat history for the model
        chat_messages = st.session_state.chat_history.get_messages()
        
        with st.spinner("Thinking..."):
            # Get response from RAG pipeline with chat history
            response = get_medical_response(query, chat_messages)
            
            # Add assistant response to chat history
            st.session_state.chat_history.add_assistant_message(response)

# Sidebar
with st.sidebar:
    st.markdown("<div class='sidebar-content'>", unsafe_allow_html=True)
    st.image("./assets/dog.jpeg", width=200)
    st.markdown("""
    **Developed by:**  
    Abhinav Kuchhal  
    CCE Department, 4th Semester  
    Registration No: 23FE10CCE00063
    """)
    st.markdown("## About")
    st.markdown("""
    This AI Medical Assistant uses advanced LLM technology 
    combined with RAG (Retrieval Augmented Generation) to provide 
    preliminary medical insights based on reported symptoms.
    
    **Disclaimer:** This tool is for informational purposes only 
    and is not a substitute for professional medical advice, 
    diagnosis, or treatment.
    """)
    
    # Optional user context (saved in session state)
    st.markdown("### Additional Information (Optional)")
    st.session_state.age = st.number_input("Age", min_value=0, max_value=120, step=1, key="age_input")
    st.session_state.gender = st.selectbox("Gender", ["", "Male", "Female", "Other"], key="gender_input")
    st.session_state.medical_history = st.multiselect(
        "Existing Medical Conditions",
        ["Diabetes", "Hypertension", "Asthma", "Heart Disease", "Cancer", "None"],
        key="medical_history_input"
    )
    st.session_state.medications = st.text_input("Current Medications (if any)", key="medications_input")
    
    # Reset button to clear the chat
    if st.button("Start New Chat"):
        st.session_state.chat_history.clear()
        st.session_state.show_welcome = True
        st.experimental_rerun()

# Main content
st.markdown("""
    <div class="title-container">
        <h1>🩺 AI-Powered Medical Assistant</h1>
    </div>
""", unsafe_allow_html=True)

# Brief introduction
st.markdown("""
    Chat with our AI assistant about your medical concerns or symptoms.
    Always consult with a healthcare professional for proper diagnosis and treatment.
""")

# Display welcome message if this is the start of a conversation
if st.session_state.show_welcome:
    render_initial_message()
    st.session_state.show_welcome = False

# Display chat history
render_chat_history(st.session_state.chat_history)

# Chat input area
st.markdown('<div class="chat-input-area">', unsafe_allow_html=True)
col1, col2 = st.columns([6, 1])
with col1:
    st.text_input(
        "Message Medical Assistant",
        key="user_input",
        on_change=handle_user_message,
        placeholder="Type your symptoms or health concerns here...",
    )
with col2:
    st.button("Send", on_click=handle_user_message, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    "<div class='footer-text'>Powered by LLaMA + RAG technology. For emergencies, call your local emergency number immediately.</div>",
    unsafe_allow_html=True
)

# Developer attribution
st.markdown("""
<div class='developer-info'>
    <strong>Developed by:</strong> Abhinav Kuchhal | CCE Department, 4th Semester | Registration No: 23FE10CCE00063
</div>
""", unsafe_allow_html=True)