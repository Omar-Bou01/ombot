"""
Professional Streamlit Chatbot Application
Powered by OpenRouter Free Models - ChatGPT Style UI
"""

import streamlit as st
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# ============================================================================
# CSS STYLING - ChatGPT Style
# ============================================================================

st.set_page_config(
    page_title="OmBot",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS for Professional Clean Design
st.markdown("""
    <style>
        /* ===== TYPOGRAPHIE - Plus Jakarta Sans ===== */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');
        
        * {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
        }
        
        /* ===== FOND PRINCIPAL ===== */
        .main {
            background: #0a0e1a !important;
        }
        
        [data-testid="stAppViewContainer"] {
            background: #0a0e1a !important;
        }
        
        /* ===== SIDEBAR ===== */
        section[data-testid="stSidebar"] {
            background: #0d1117 !important;
            border-right: 1px solid rgba(255,255,255,0.07);
        }
        
        section[data-testid="stSidebar"] > div {
            background: #0d1117 !important;
        }
        
        /* Titre HISTORY */
        section[data-testid="stSidebar"] h3 {
            color: #64748b !important;
            font-size: 11px !important;
            font-weight: 500 !important;
            letter-spacing: 0.1em !important;
            text-transform: uppercase !important;
            margin-top: 1rem !important;
        }
        
        /* Bouton New Chat - Outline style */
        section[data-testid="stSidebar"] .stButton button:first-of-type,
        section[data-testid="stSidebar"] > div > div > div > div > div > div:first-child button {
            background: transparent !important;
            color: #00c896 !important;
            border: 1.5px solid #00c896 !important;
            border-radius: 10px !important;
            padding: 0.65rem 1rem !important;
            font-weight: 500 !important;
            font-size: 14px !important;
            width: 100%;
            transition: all 0.2s ease !important;
        }
        
        section[data-testid="stSidebar"] .stButton button:first-of-type:hover {
            background: rgba(0, 200, 150, 0.15) !important;
            transform: translateY(-1px);
        }
        
        /* Boutons historique */
        section[data-testid="stSidebar"] .stButton button {
            background: transparent !important;
            color: #64748b !important;
            border: 1px solid rgba(255,255,255,0.05) !important;
            border-radius: 8px !important;
            padding: 0.6rem 0.9rem !important;
            font-weight: 400 !important;
            font-size: 13px !important;
            text-align: left !important;
            transition: all 0.2s ease !important;
        }
        
        section[data-testid="stSidebar"] .stButton button:hover {
            background: rgba(255,255,255,0.03) !important;
            border-color: rgba(0,200,150,0.3) !important;
            color: #f1f5f9 !important;
        }
        
        /* Cacher la section Settings */
        section[data-testid="stSidebar"] .element-container:has(.stSuccess) { display: none !important; }
        section[data-testid="stSidebar"] .element-container:has(.stError) { display: none !important; }
        section[data-testid="stSidebar"] .element-container:has(.stSelectbox) { display: none !important; }
        section[data-testid="stSidebar"] .stCaption { display: none !important; }
        
        /* Divider sidebar */
        section[data-testid="stSidebar"] hr {
            border-color: rgba(255,255,255,0.07) !important;
            margin: 1.5rem 0 !important;
        }
        
        /* ===== PAGE PRINCIPALE ===== */
        
        /* Titre principal Bonjour */
        .main h1 {
            font-size: 52px !important;
            font-weight: 300 !important;
            color: #ffffff !important;
            text-align: center !important;
            margin-bottom: 0.5rem !important;
            margin-top: 3rem !important;
        }
        
        /* Sous-titre */
        .main p {
            color: #64748b !important;
            font-size: 16px !important;
            text-align: center !important;
            margin-bottom: 3rem !important;
        }
        
        /* Boutons de suggestions - Page principale uniquement */
        .main .stButton > button {
            background: #141c2e !important;
            border: 1px solid rgba(255,255,255,0.08) !important;
            color: #e2e8f0 !important;
            border-radius: 12px !important;
            padding: 20px !important;
            width: 100% !important;
            font-size: 14px !important;
            font-weight: 400 !important;
            transition: all 0.2s ease !important;
            text-align: center !important;
            height: auto !important;
            min-height: 60px !important;
        }
        
        .main .stButton > button:hover {
            border-color: rgba(0,200,150,0.5) !important;
            transform: translateY(-2px) !important;
            background: #1a2438 !important;
        }
        
        /* ===== CHAMP DE MESSAGE ===== */
        .stChatInput input,
        .stTextInput > div > div > input {
            background: #141c2e !important;
            border: 1px solid rgba(255,255,255,0.1) !important;
            border-radius: 16px !important;
            color: #f1f5f9 !important;
            padding: 16px 20px !important;
            font-size: 15px !important;
        }
        
        .stChatInput input:focus,
        .stTextInput > div > div > input:focus {
            border-color: #00c896 !important;
            box-shadow: 0 0 0 1px #00c896 !important;
        }
        
        .stChatInput input::placeholder {
            color: #64748b !important;
        }
        
        /* ===== MESSAGES - Force proper layout ===== */
        [data-testid="stChatMessage"] {
            background: transparent !important;
            padding: 1rem 0 !important;
            display: flex !important;
            flex-direction: row !important;
            align-items: flex-start !important;
            gap: 1rem !important;
            width: 100% !important;
        }

        /* Avatar container - fixed size on the left */
        [data-testid="stChatMessage"] > div:first-child {
            flex-shrink: 0 !important;
            width: 2.5rem !important;
            height: 2.5rem !important;
            min-width: 2.5rem !important;
            margin-right: 0.5rem !important;
            position: relative !important;
        }

        /* Content container - takes remaining space */
        [data-testid="stChatMessage"] > div:last-child {
            flex: 1 1 auto !important;
            min-width: 0 !important;
            max-width: calc(100% - 3.5rem) !important;
            overflow-wrap: break-word !important;
            word-break: break-word !important;
        }
        
        /* Text inside messages */
        [data-testid="stChatMessage"] p {
            color: #f1f5f9 !important;
            font-size: 15px !important;
            line-height: 1.6 !important;
            text-align: left !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        
        /* Force avatar image to stay in bounds */
        [data-testid="stChatMessage"] img {
            max-width: 2.5rem !important;
            max-height: 2.5rem !important;
            border-radius: 50% !important;
        }
        
        /* ===== SCROLLBAR ===== */
        ::-webkit-scrollbar {
            width: 6px;
        }
        
        ::-webkit-scrollbar-track {
            background: transparent;
        }
        
        ::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(255, 255, 255, 0.15);
        }
        
        /* ===== GÉNÉRAL ===== */
        .block-container {
            padding-top: 3rem !important;
            max-width: 900px !important;
        }
        
        /* Success/Error messages */
        .stSuccess, .stError {
            background: rgba(0, 200, 150, 0.1) !important;
            border: 1px solid rgba(0, 200, 150, 0.3) !important;
            border-radius: 10px !important;
            color: #f1f5f9 !important;
        }
        
        .stError {
            background: rgba(239, 68, 68, 0.1) !important;
            border-color: rgba(239, 68, 68, 0.3) !important;
        }
        
        /* Spinner */
        .stSpinner > div {
            border-color: #00c896 transparent transparent transparent !important;
        }
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

@st.cache_data
def get_available_models():
    """Fetch available free models from OpenRouter"""
    try:
        response = requests.get(
            "https://openrouter.ai/api/v1/models",
            timeout=5
        )
        if response.status_code == 200:
            models = response.json().get("data", [])
            # Filter free models
            free_models = [m for m in models if m.get("pricing", {}).get("prompt") == "0"]
            return [(m["id"], m["name"]) for m in free_models[:15]]
    except:
        pass
    return []

def generate_conversation_title(text):
    """Generate a title from the first user message"""
    return text[:30] + "..." if len(text) > 30 else text


def get_api_key():
    """Return API key from Streamlit secrets (deploy) or env vars (local)."""
    try:
        secret_key = st.secrets.get("OPENROUTER_API_KEY", "")
        if secret_key:
            return secret_key
    except Exception:
        pass

    return os.getenv("OPENROUTER_API_KEY", "")

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================

# Initialize session state for conversations
if "conversations" not in st.session_state:
    st.session_state.conversations = {}

if "current_conversation_id" not in st.session_state:
    # Create first conversation
    conv_id = datetime.now().strftime("%Y%m%d_%H%M%S")
    st.session_state.conversations[conv_id] = {
        "title": "New Chat",
        "messages": [],
        "timestamp": datetime.now()
    }
    st.session_state.current_conversation_id = conv_id

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "openrouter/auto"


# ============================================================================
# PAGE CONFIGURATION (Already done in CSS section)
# ============================================================================

# ============================================================================
# SIDEBAR - Chat History & Settings  
# ============================================================================

with st.sidebar:
    # New Chat Button
    if st.button("+ New Chat", use_container_width=True, key="new_chat_btn"):
        conv_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        st.session_state.conversations[conv_id] = {
            "title": "New Chat",
            "messages": [],
            "timestamp": datetime.now()
        }
        st.session_state.current_conversation_id = conv_id
        st.rerun()
    
    st.divider()
    
    # Chat History
    st.markdown("### History")
    
    # Sort conversations by timestamp (most recent first)
    sorted_convs = sorted(
        st.session_state.conversations.items(),
        key=lambda x: x[1]["timestamp"],
        reverse=True
    )
    
    for conv_id, conv_data in sorted_convs:
        is_active = conv_id == st.session_state.current_conversation_id
        
        col1, col2 = st.columns([0.85, 0.15])
        
        with col1:
            if st.button(
                f"{conv_data['title']}",
                use_container_width=True,
                key=f"conv_{conv_id}",
                help=conv_data['title']
            ):
                st.session_state.current_conversation_id = conv_id
                st.rerun()
        
        with col2:
            if st.button("×", key=f"del_{conv_id}"):
                del st.session_state.conversations[conv_id]
                if st.session_state.current_conversation_id == conv_id:
                    st.session_state.current_conversation_id = sorted_convs[0][0] if sorted_convs else None
                st.rerun()
    




# ============================================================================
# MAIN CHAT INTERFACE - ChatGPT Style
# ============================================================================

# Get current conversation
current_conv = st.session_state.conversations[st.session_state.current_conversation_id]
current_messages = current_conv["messages"]

# Display messages
if current_messages:
    for message in current_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
else:
    # Welcome screen - Clean and Professional
    st.markdown("# Bonjour")
    st.markdown("Comment puis-je vous aider aujourd'hui ?")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Boutons de suggestions en 2 colonnes
    col1, col2 = st.columns(2)
    
    suggestion_prompts = {
        "sug1": "Aide-moi à résumer un document",
        "sug2": "Aide-moi à générer du code",
        "sug3": "J'ai besoin d'aide pour traduire un texte",
        "sug4": "J'ai besoin d'aide pour analyser des données"
    }
    
    with col1:
        if st.button("Résumer un document", key="sug1", use_container_width=True):
            # Stocker le message à traiter
            if "pending_message" not in st.session_state:
                st.session_state.pending_message = suggestion_prompts["sug1"]
                st.rerun()
        if st.button("Traduire un texte", key="sug3", use_container_width=True):
            if "pending_message" not in st.session_state:
                st.session_state.pending_message = suggestion_prompts["sug3"]
                st.rerun()
    
    with col2:
        if st.button("Générer du code", key="sug2", use_container_width=True):
            if "pending_message" not in st.session_state:
                st.session_state.pending_message = suggestion_prompts["sug2"]
                st.rerun()
        if st.button("Analyser des données", key="sug4", use_container_width=True):
            if "pending_message" not in st.session_state:
                st.session_state.pending_message = suggestion_prompts["sug4"]
                st.rerun()

st.divider()

# ============================================================================
# CHAT INPUT AND API CALL
# ============================================================================

# Chat input
user_input = st.chat_input("Type your message...", key="chat_input")

# Check if a suggestion button was clicked
if "pending_message" in st.session_state and st.session_state.pending_message:
    user_input = st.session_state.pending_message
    del st.session_state.pending_message

if user_input:
    api_key = get_api_key()
    
    if not api_key:
        st.error("""
        **API Key Not Configured**
        
        Please set up your OpenRouter API key:
        
        **For Streamlit Cloud deployment:**
        1. Open app settings → **Secrets**
        2. Add: `OPENROUTER_API_KEY="your_api_key"`
        3. Save and restart the app
        
        **For local development:**
        1. Create a `.env` file in the project directory
        2. Add: `OPENROUTER_API_KEY=your_api_key`
        3. Restart the app
        """)
    else:
        # Add user message to conversation history
        current_messages.append({
            "role": "user",
            "content": user_input
        })
        
        # Update conversation title if it's the first message
        if len(current_messages) == 1:
            current_conv["title"] = generate_conversation_title(user_input)
        
        # Display user message in chat
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Show loading spinner while waiting for response
        with st.spinner("Thinking..."):
            try:
                # Make API request to OpenRouter
                response = requests.post(
                    url="https://openrouter.ai/api/v1/chat/completions",
                    headers={
                        "Authorization": f"Bearer {api_key}",
                        "HTTP-Referer": "http://localhost:8501",
                        "X-Title": "Streamlit Chatbot",
                    },
                    json={
                        "model": st.session_state.selected_model,
                        "messages": current_messages,
                        "temperature": 0.7,
                        "max_tokens": 1500,
                    },
                    timeout=30,
                )
                
                # Handle successful API response
                if response.status_code == 200:
                    data = response.json()
                    
                    # Extract assistant message from API response
                    assistant_message = data["choices"][0]["message"]["content"]
                    
                    # Add assistant message to conversation history
                    current_messages.append({
                        "role": "assistant",
                        "content": assistant_message
                    })
                    
                    # Display assistant message in chat
                    with st.chat_message("assistant"):
                        st.markdown(assistant_message)
                    
                    # Rerun to update the sidebar
                    st.rerun()
                
                # Handle API errors
                else:
                    error_detail = response.text
                    st.error(f"""
                    **API Error**
                    
                    **Status Code:** {response.status_code}
                    
                    **Details:** 
                    ```
                    {error_detail}
                    ```
                    """)
            
            # Handle network errors
            except requests.exceptions.Timeout:
                st.error("**Request Timeout** - The request took too long. Please try again.")
            except requests.exceptions.ConnectionError:
                st.error("**Connection Error** - Could not connect to the API. Check your internet.")
            # Handle other exceptions
            except Exception as e:
                st.error(f"**Unexpected Error** - {str(e)}")
