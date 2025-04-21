class ChatHistory:
    """
    Manages the conversation history between user and AI assistant.
    """
    def __init__(self):
        self.messages = []
        
    def add_user_message(self, message):
        """Add a user message to the chat history."""
        self.messages.append({"role": "user", "content": message})
        
    def add_assistant_message(self, message):
        """Add an assistant message to the chat history."""
        self.messages.append({"role": "assistant", "content": message})
        
    def get_messages(self):
        """Get all messages in the chat history."""
        return self.messages
    
    def get_context_for_llm(self, max_messages=10):
        """
        Format recent chat history for the LLM context window.
        Limits the number of messages to prevent context overflow.
        """
        # Take the most recent messages up to max_messages
        recent_messages = self.messages[-max_messages:] if len(self.messages) > max_messages else self.messages
        
        # Format as a string for context
        context = ""
        for msg in recent_messages:
            prefix = "User: " if msg["role"] == "user" else "Assistant: "
            context += f"{prefix}{msg['content']}\n\n"
            
        return context
    
    def clear(self):
        """Clear the chat history."""
        self.messages = []