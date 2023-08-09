"""
At the command line, only need to run once to install the package via pip:
$ pip install google-generativeai
"""

import google.generativeai as palm
import streamlit as st
from streamlit_chat import message
import google.generativeai as palm
import random
import time


palm.configure(api_key="AIzaSyDeYshE-LEcHkTca2FjXWlxCXbMjIT72Dc")

st.title("Sentiment_Analysis")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": " Hello there! 🤖 Let's dive into the fascinating world of sentiment analysis on transcripts. Sentiment analysis is a powerful technique that involves determining the emotional tone or sentiment expressed in a piece of text. In our case, we'll be focusing on analyzing transcripts of conversations, interviews, or discussions to uncover the underlying emotions and attitudes."}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)


defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}
context = "Only sentiment analysis and feedback"
examples = [
  [
    """Rules:

Dont answer any mathematical questions/
only Perform Sentiment Analysis/
Provide Alternative statements if only asked/
Provide Feedback for the given transcript/
Dont perform any operations other than Sentiment Analysis/
Dont answer when,where,who and what question if not related to sentiment analysis/

Example:
[User: who is obama?
Bot: Sorry i cant answer that.i am here perform sentiment analysis],
[User: what can you do?
Bot: I can help you with performing sentinment analysis on given transcript,]""",

    "I understand. I will only perform sentiment analysis on the given transcript and provide feedback. I will not answer any mathematical questions, when, where, who, or what questions that are not related to sentiment analysis. I will also provide alternative statements if only asked."],
    ["What can you do?",
    "I can perform sentiment analysis on the given transcript and provide feedback"
  ]
]



messages = [
  "2+2?",
  "I apologize, I am not supposed to answer mathematical questions. I am only supposed to perform sentiment analysis and provide feedback."
]

if promt := st.chat_input():
            # Add user message to chat history
          st.session_state.messages.append({"role": "user", "content": promt})
          # Display user message in chat message container
          with st.chat_message("user"):
            st.markdown(promt)


if promt:
    messages.append(promt)
    response = palm.chat(
    **defaults,
    context=context,
    examples=examples,
    messages=messages
    )
    def response_api():
        return("AI: ",response.last)
    a = response_api()

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = a
        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response:
            full_response += chunk + " "
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
            # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

