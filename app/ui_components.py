import streamlit as st
import os

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
    # Try to load external CSS file
    css_path = os.path.join("assets", "css", "custom.css")
    
    if os.path.exists(css_path):
        with open(css_path, "r") as f:
            css_content = f.read()
        st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    else:
        # Fallback to simple inline CSS if file doesn't exist
        st.markdown("""
        <style>
        /* Base Styles */
        .stApp {
            background-color: #0a1929;
            color: #e0e0e0;
        }
        
        /* Chat Container */
        .chat-container {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 15px;
        }
        
        /* Message Styling */
        .chat-message {
            display: flex;
            align-items: flex-start;
            padding: 8px;
            border-radius: 6px;
            max-width: 85%;
        }
        
        .user-message {
            margin-left: auto;
            background-color: #1e4976;
            border-left: 2px solid #4d94ff;
        }
        
        .assistant-message {
            margin-right: auto;
            background-color: #112940;
            border-right: 2px solid #4d94ff;
        }
        
        .avatar {
            width: 30px;
            height: 30px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            margin-right: 8px;
        }
        
        .user-avatar {
            background-color: #2a5a9a;
        }
        
        .assistant-avatar {
            background-color: #1c3b5a;
        }
        
        .message-content {
            flex: 1;
            padding: 3px;
            color: #e0e0e0;
        }
        
        /* Input Area */
        .chat-input-area {
            display: flex;
            background-color: #112940;
            padding: 10px;
            border-radius: 8px;
            margin-top: 10px;
            border: 1px solid #1e4976;
        }
        
        /* Other UI Elements */
        .title-container {
            margin-bottom: 15px;
        }
        
        .footer-text {
            font-size: 12px;
            color: #b0b0b0;
            text-align: center;
            margin-top: 15px;
        }
        
        .developer-info {
            background-color: #15375e;
            padding: 10px;
            border-radius: 5px;
            margin-top: 15px;
            text-align: center;
            border-left: 4px solid #4d94ff;
            color: #ffffff;
        }
        
        /* Override Streamlit elements */
        .stButton>button {
            background-color: #4d94ff;
            color: #ffffff;
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;
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