import streamlit as st

def render_chat_message(message, is_user=True):
    """
    Render a chat message with appropriate styling based on sender.
    
    Args:
        message (str): The message content
        is_user (bool): True if message is from user, False if from assistant
    """
    if is_user:
        st.markdown(f"""
        <div class="chat-message user-message">
            <div class="avatar user-avatar">👤</div>
            <div class="message-content">{message}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message assistant-message">
            <div class="avatar assistant-avatar">🩺</div>
            <div class="message-content">{message}</div>
        </div>
        """, unsafe_allow_html=True)

def render_chat_history(chat_history):
    """
    Render the full chat history.
    
    Args:
        chat_history (ChatHistory): Instance containing conversation messages
    """
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    
    for message in chat_history.get_messages():
        is_user = message["role"] == "user"
        render_chat_message(message["content"], is_user)
    
    st.markdown('</div>', unsafe_allow_html=True)

def load_custom_css():
    """Load custom CSS for the chat interface."""
    st.markdown("""
    <style>
    /* Base Styles */
    .main {
        padding: 2rem;
        color: #e0e0e0;
    }
    .stApp {
        background-color: #0a1929;
    }
    
    /* Chat Container */
    .chat-container {
        display: flex;
        flex-direction: column;
        gap: 15px;
        margin-bottom: 20px;
    }
    
    /* Message Styling */
    .chat-message {
        display: flex;
        align-items: flex-start;
        padding: 10px;
        border-radius: 8px;
        max-width: 80%;
        animation: fadeIn 0.3s ease-in-out;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .user-message {
        margin-left: auto;
        background-color: #1e4976;
        border-top-right-radius: 2px;
        border-left: 2px solid #4d94ff;
    }
    
    .assistant-message {
        margin-right: auto;
        background-color: #112940;
        border-top-left-radius: 2px;
        border-right: 2px solid #4d94ff;
    }
    
    .avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        margin-right: 10px;
    }
    
    .user-avatar {
        background-color: #2a5a9a;
    }
    
    .assistant-avatar {
        background-color: #1c3b5a;
    }
    
    .message-content {
        flex: 1;
        padding: 5px;
        color: #e0e0e0;
    }
    
    /* Input Area */
    .chat-input-area {
        display: flex;
        background-color: #112940;
        padding: 10px;
        border-radius: 10px;
        margin-top: 20px;
        border: 1px solid #1e4976;
    }
    
    /* Other UI Elements */
    .diagnosis-box {
        background-color: #112940;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        margin-top: 20px;
        color: #e0e0e0;
        border-left: 4px solid #4d94ff;
    }
    
    .title-container {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        color: #ffffff;
    }
    
    .footer-text {
        font-size: 14px;
        color: #b0b0b0;
        text-align: center;
        margin-top: 30px;
    }
    
    .sidebar-content {
        padding: 20px;
        color: #e0e0e0;
    }
    
    .developer-info {
        background-color: #15375e;
        padding: 15px;
        border-radius: 5px;
        margin-top: 20px;
        text-align: center;
        border-left: 4px solid #4d94ff;
        color: #ffffff;
    }
    
    /* Override Streamlit elements */
    .stTextInput, .stTextArea, .stSelectbox {
        background-color: #112940;
        color: #ffffff;
    }
    
    .stButton>button {
        background-color: #4d94ff;
        color: #ffffff;
    }
    
    .stExpander {
        background-color: #112940;
        color: #e0e0e0;
    }
    
    .stMarkdown {
        color: #e0e0e0;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    
    /* Chat input styling */
    #chat-input-text {
        flex-grow: 1;
        margin-right: 10px;
    }
    
    #send-button {
        min-width: 100px;
    }
    </style>
    """, unsafe_allow_html=True)

def render_initial_message():
    """Render the welcome message from the AI assistant."""
    st.markdown(f"""
    <div class="chat-message assistant-message">
        <div class="avatar assistant-avatar">🩺</div>
        <div class="message-content">
            <p>Hello! I'm your Medical Assistant. How are you feeling today?</p>
            <p>Please describe any symptoms you're experiencing, and I'll try to provide some helpful information.</p>
            <small><em>Remember: I'm here to provide information, not medical diagnosis. Always consult with a healthcare professional for proper medical advice.</em></small>
        </div>
    </div>
    """, unsafe_allow_html=True)