import os
import streamlit as st
from streamlit_chat import message
import random
import time
import replicate
os.environ['REPLICATE_API_TOKEN'] = "r8_PQf4tOQpuubVsm0gfDvkkbwW8tu2HgI2Cag1K"

st.title("Sentiment_Analysis")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if promt := st.chat_input():
            # Add user message to chat history
          st.session_state.messages.append({"role": "user", "content": promt})
          # Display user message in chat message container
          with st.chat_message("user"):
            st.markdown(promt)



# Prompts
pre_prompt = """Rules:

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
The provided transcript reflects a positive and proactive attitude, effectively communicating the individual's strengths and aspirations. The use of language is engaging and showcases their commitment to professional growth. The mention of "simplify the mode of input without compromising the output" is an interesting point, as it suggests a focus on efficiency and optimization. Overall, a well-rounded statement that presents the individual in a favorable light.]"""
def gen_response(promt):
  prompt_input = promt

  # Generate LLM response
  output = replicate.run('a16z-infra/llama13b-v2-chat:df7690f1994d94e96ad9d568eac121aecf50684a0b0963b25a41cc40061269e5', # LLM model
                          input={"prompt": f"{pre_prompt} {prompt_input} Assistant: ", # Prompts
                          "temperature":0.4, "top_p":0.9, "max_length":1028, "repetition_penalty":1})  # Model parameters
  return output

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = gen_response(promt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)

