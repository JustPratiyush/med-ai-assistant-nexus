import ollama

def query_llama(prompt, system_prompt="", chat_history=None):
    """
    Send a prompt to the Llama model with chat history and return its response.
    
    Args:
        prompt (str): The user's current query
        system_prompt (str): System instructions for the model
        chat_history (list): List of previous messages in the conversation
        
    Returns:
        str: The model's response
    """
    # Create messages array starting with system prompt if provided
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    
    # Add chat history if provided
    if chat_history and len(chat_history) > 0:
        messages.extend(chat_history)
    
    # Add current prompt
    messages.append({"role": "user", "content": prompt})
    
    # Query the model
    response = ollama.chat(model="llama3.2:latest", messages=messages)
    return response["message"]["content"]

def generate_medical_response(symptoms, retrieved_context, chat_history=None):
    """
    Generate a comprehensive medical response by combining RAG results with model knowledge.
    
    Args:
        symptoms (str): The user's described symptoms
        retrieved_context (str): Retrieved medical information from database
        chat_history (list): Previous conversation messages
    
    Returns:
        str: AI-generated medical response
    """
    system_prompt = """You are an AI medical assistant providing information based on symptoms.
    Always combine information from your medical knowledge and the retrieved data.
    Maintain a conversational tone while being informative and precise.
    Be clear that you're not providing medical diagnosis, just information.
    If you don't know something, say so rather than making it up.
    Focus on being helpful and accurate."""
    
    prompt = f"""
    Based on the conversation history and the current symptoms described, provide helpful medical information.
    
    User's symptoms or question: {symptoms}
    
    Retrieved medical information:
    {retrieved_context}
    
    Provide a balanced response that:
    1. Addresses the specific concern using both retrieved information and medical knowledge
    2. Suggests possible causes or conditions (without guaranteeing diagnosis)
    3. Recommends appropriate next steps or general advice
    4. Mentions when professional medical attention should be sought
    
    Keep your response conversational but informative.
    """
    
    return query_llama(prompt, system_prompt, chat_history)