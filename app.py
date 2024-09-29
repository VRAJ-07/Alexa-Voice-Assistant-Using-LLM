import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import os
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    # Set Hugging Face or Groq API tokens
    os.environ['GROQ_API_KEY'] = 'API_KEY'

    # Define the prompt template
    prompt = PromptTemplate(
        input_variables=["user_message"],
        template="You are a virtual assistant named Alexa skilled in general tasks like Alexa, Siri and Google Assistant. {user_message}"
    )

    # Initialize the LLM using ChatGroq
    llm = ChatGroq(
        temperature=0,  # Adjust the temperature as per the need
        groq_api_key=os.environ['GROQ_API_KEY'],
        model_name='llava-v1.5-7b-4096-preview',
        max_tokens=200
    )

    # Create the LLMChain for running the conversation
    retrieval_chain = (
        {"user_message": RunnablePassthrough()}  # Capture the user's input
        | prompt  # Use the prompt template to format the assistant's response
        | llm  # Pass the input to the LLM for generating a response
        | StrOutputParser()  # Convert the response to a string
    )

    # Define the user input as in your original example
    user_input = command

    # Call the chain and get the result
    result = retrieval_chain.invoke({"user_message": user_input})

    # Print the result
    return result

def processCommand(c):
    if "stop" in c.lower():
        speak("Goodbye! Have a great day.")
        exit()  # Stop the program
    elif "open google" in c.lower():
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
        speak("Opening Youtube")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        speak("Opening Linkedin")
    elif c.lower().startswith("play "):
        song_name = c.lower().split("play ")[1].strip()
        link = musicLibrary.get_music_link(song_name)  # Use the corrected function name
        if link:
            webbrowser.open(link)
            speak(f"Playing {song_name}.")
        else:
            speak("Sorry, I couldn't find that song.")
    else:
        # Let LLM handle the command
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Alexa....")
    while True:
        # Listen for the wake word 'Alexa'
        # obtain audio from the microphone
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=2)
            command = recognizer.recognize_google(audio)
            if command.lower() == "alexa":
                speak("Yes? How can I help you?")
                # Listen for command
                with sr.Microphone() as source:
                    print("Alexa Active...")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
