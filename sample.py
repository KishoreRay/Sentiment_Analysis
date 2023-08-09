"""
At the command line, only need to run once to install the package via pip:
$ pip install google-generativeai
"""

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

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.55,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
  'max_output_tokens': 1024,
  'stop_sequences': [],
  'safety_settings': [],
}
if promt := st.chat_input():
            # Add user message to chat history
          st.session_state.messages.append({"role": "user", "content": promt})
          # Display user message in chat message container
          with st.chat_message("user"):
            st.markdown(promt)
if promt:
            prompt = f""" Rules:

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
            Bot: I can help you with performing sentinment analysis on given transcript,]
            [User: I am a highly motivated and adaptable student with a strong passion fortechnology and a solid foundation in computer science with goodjudgment, and time management skills. Love to learn about newtechnologies. Aiming to leverage my abilities to successfully fill thevacancy at your company. Dependable and reliable, ready to learn andgrow with your company. Always try to simplify the mode of input withoutcompromising the output.
            Bot: 
            Sentiment Analysis:
            The provided text seems to express a positive sentiment. The individual appears enthusiastic and dedicated, showcasing their passion for technology and their background in computer science. They also highlight their time management skills, willingness to learn, and their aim to contribute effectively to the company. The statement indicates a strong sense of motivation and adaptability.
            Feedback:
            The provided transcript reflects a positive and proactive attitude, effectively communicating the individual's strengths and aspirations. The use of language is engaging and showcases their commitment to professional growth. The mention of "simplify the mode of input without compromising the output" is an interesting point, as it suggests a focus on efficiency and optimization. Overall, a well-rounded statement that presents the individual in a favorable light.]
            
            input: hi
            output: how can i help you
            input: {promt}
            output:"""

            response = palm.generate_text(
            **defaults,
            prompt=prompt
            )
            
            def response_api():
                return("AI: ",response.result)
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


        
