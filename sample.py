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
            prompt = f""" Sentiment Explanation:
            The text expresses overwhelmingly positive sentiments. Words like "wonderful," "amazing," "perfect," and "delicious" indicate a strong positive tone. The overall sentiment of the text is positive with a high confidence score of 0.92.

            Feedback:
            The sentiment analysis model has successfully captured the positive emotions conveyed in the text. It accurately identified the positive sentiments expressed by using words with strong positive connotations. The high confidence score of 0.92 indicates that the model is quite confident in its classification. However, it's important to note that sentiment analysis can be influenced by the context and language used, so occasional misinterpretations may occur. Nevertheless, this result is consistent with the evident positivity of the given text.
            input: I agree with time magazines assessment.  They are exciting because they bring a lot of freshness to the workplace which helps us to do better. They are also threatening because of their lack of longer commitment and emotional weakness in the workplace.
            They deserve to be recognized as change force, but they don't really justify the hype given.
            The Fresh workforce brings lots of unconventional ideas, work practices, and huge expectations. Their inherent assumption and/or desire that everything needs to be changed should be tamed. Their lack of understanding of the complex problem is worrisome. They are not very good at making tradeoffs. They want everything at the same time which is a disregard for natural evolution.
            output: Sentiment Explanation:
            The text presents a mixed sentiment with both positive and negative aspects. The positive sentiment is evident in phrases like "exciting," "bring a lot of freshness," and "helps us to do better," indicating enthusiasm towards the Fresh workforce's impact. On the other hand, negative sentiments are expressed through phrases like "threatening," "lack of longer commitment," "emotional weakness," "lack of understanding," and "not very good at making tradeoffs," which point to concerns and drawbacks associated with the Fresh workforce.

            Feedback:
            The sentiment analysis model has successfully captured the mixed sentiments in the text. It correctly identified the positive aspects related to the Fresh workforce, such as their excitement and ability to bring freshness and improvement to the workplace. Simultaneously, the model also recognized the negative aspects, including concerns about their shorter commitment, emotional weakness, and difficulty with trade-offs.  
            input: Nowadays this is actually not much needed in my opinion. Everything is available with lot of analytics built in, they have access to all information on the internet so, it is not required to give person-to-person, hand-to-hand. 40% old timers are ready to mentor provided the wavelengths match.
            output: 
            Sentiment Explanation:
            The text conveys a neutral sentiment, which means it lacks strong positive or negative emotions. The overall tone appears to be matter-of-fact and informative, without expressing a particular emotional bias. The statements present a balanced view, discussing the availability of information through analytics and the internet, as well as the readiness of some old-timers to mentor under certain conditions.

            Feedback:
            The sentiment appears to be positive overall, with several positive expressions such as "highly motivated," "strong passion for technology," "solid foundation," "excellent judgment," "eager to learn," "excited to leverage my abilities," and "let's make great things together!" These phrases convey enthusiasm, dedication, and a positive attitude.
            input:I am a highly motivated and adaptable student with a strong passion fortechnology and a solid foundation in computer science with goodjudgment, and time management skills. Love to learn about newtechnologies. Aiming to leverage my abilities to successfully fill thevacancy at your company. Dependable and reliable, ready to learn andgrow with your company. Always try to simplify the mode of input withoutcompromising the output.(can suggest any short alternate method to express the same?)
            output:As a highly motivated and adaptable student, I have a strong passion for technology and a solid foundation in computer science. With excellent judgment and time management skills, I am always eager to learn about new technologies. I am excited to leverage my abilities and grow with your company, bringing a dependable and reliable approach to simplify input without compromising output. Let's make great things together!

            Feedback:
            The sentiment analysis model has correctly identified the neutral sentiment in the text. The absence of strong emotions or subjective opinions in the text supports the neutral sentiment classification. 
            input: from personal experience – working from home well over 10 years now – one imp thing is trust. Work-life balance works only if employees are trusted. If they are not trusted, they will act untrustworthy way. In millennial generation – we had parental leaves, flexible working hours, 13 day fortnight (you work extra hours every day to get every second Friday as off) and flexibility in holidays. So, work-life balance tends to revolves around the flexibility and revolves around being trusted. 
            output: Sentiment Explanation:
            The text conveys a positive sentiment, which reflects a favorable view towards the importance of trust and work-life balance in the context of remote work. Positive language is evident in phrases like "important thing is trust," "work-life balance works only if employees are trusted," and "work-life balance tends to revolve around flexibility and being trusted."

            Feedback:
            The sentiment analysis model has accurately identified the positive sentiment in the text. The expressions used in the text reflect a positive outlook towards the role of trust and flexibility in maintaining a healthy work-life balance in a remote work environment. 
            input: The main challenge is to make them understand the work and what has to be delivered professionally. The understanding process is much faster but it takes more time to set expectations with them. Once they understand they proceed and are committed but the initial process is very challenging. They demand more information for the work required, they do not like to be given part or piecemeal information. They want the complete holistic picture and to their satisfaction. Only then do they start working which gets tedious at times when there are strict deadlines and someone wants to research on tertiary unimportant aspects.  They cannot be enforced, they want complete guidance and information, and then they deliver very well above expectations. -(can you suggest some positive words for the above negative context)"
            output: Certainly! Here are some positive words and phrases that can be used to reframe the negative context:

            1. Opportunity (instead of challenge)
            2. Efficient (instead of takes more time)
            3. Inquisitive (instead of demanding)
            4. Engaging (instead of tedious)
            5. Ambitious goals (instead of strict deadlines)
            6. Key aspects (instead of tertiary unimportant aspects)
            7. Self-motivated (instead of cannot be enforced)
            8. Thorough understanding (instead of want complete guidance and information)
            9. Thorough research (instead of research on tertiary unimportant aspects)
            10. Proactive (instead of excessive information-seeking)
            11. Focus on priorities (instead of consequences of focusing too much)
            12. Deliberate decision-making (instead of stuck in analysis paralysis)

            By using more positive language, you can shift the perspective and promote a more constructive and optimistic outlook on the situation. This can help create a more productive and harmonious work environment.
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


        