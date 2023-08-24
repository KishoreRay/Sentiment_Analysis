# Sentiment Analysis Chat Interface
This project implements a chat interface for sentiment analysis using the Google Generative AI package and Streamlit. The interface allows users to input text, which is then analyzed for sentiment, and feedback is provided. The primary goal of this project is to showcase the capabilities of sentiment analysis in a user-friendly and interactive manner.

# Table of Contents
* What It Does
* Getting Started
* Prerequisites
* Installation
* Usage
* Configuration
* Example Transcripts
* Clear Chat History


# What It Does
The Sentiment Analysis Chat Interface lets users interact with an AI assistant to perform sentiment analysis on text input. The AI assistant uses the Google Generative AI package to analyze the input text and provide feedback on the emotional tone expressed within the text. The project demonstrates how AI can be utilized to gain insights into the sentiment and emotional content of textual conversations, interviews, discussions, and more.

The user can input text messages into the chat interface, and the AI assistant responds with sentiment analysis results. The project emphasizes the following functionalities:

* Sentiment Analysis: The core feature is sentiment analysis, where the AI assistant evaluates the emotional tone of the input text, indicating whether the text expresses positive, negative, or neutral sentiments.

* Feedback: The assistant offers feedback based on the sentiment analysis results. It helps the user understand the underlying emotional content of the text and can provide alternative statements if requested.

* Interactive Chat Interface: The Streamlit-based interface provides an interactive chat-like experience, simulating a conversation between the user and the AI assistant.
  abilities of sentiment analysis and provide an interactive way to engage with the analysis process.


# Getting Started
* Prerequisites: 
    Before running the project, you'll need to have the following software installed:
    Python 3.x
  
* Install the required packages using pip:
<pre>pip install -r requirements.txt</pre>


## Usage
Run the Streamlit app:
<pre>streamlit run app.py</pre>
* Open your web browser and navigate to the provided URL (usually http://localhost:8008).
  You'll see the chat interface for sentiment analysis. Input your text and interact with the assistant to receive sentiment analysis feedback.

## Configuration
In the app.py file, you can configure the default settings for the chat interface. These settings include the model to use, temperature, candidate count, top-k, and top-p values.

<pre>defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}</pre>

## Clear Chat History
The chat history can be cleared by clicking the "Clear Chat History" button in the sidebar.

# Future Scopes
The project has several exciting future scopes:

* Voice Compatibility: Expanding the project to support voice inputs would enhance its usability. Users could speak their sentences, and the AI could analyze sentiment not just from the text but also from the tone of voice.

* Tone Analysis: Integrating tone analysis capabilities could allow the AI to assess sentiment through tone, adding an extra layer of depth to the analysis.

* Interview Chat Bot: This project could be extended to develop an interview chat bot. The AI could simulate interview scenarios, assess the sentiment of the interviewee's responses, and provide feedback to both the interviewer and the interviewee.
