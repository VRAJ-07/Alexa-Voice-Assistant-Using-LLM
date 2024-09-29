# Alexa-Voice-Assistant-Using-LLM

This repository contains the source code for **Alexa**, a virtual assistant developed using Python. The assistant integrates speech recognition, web automation, music playback, and natural language processing through Groq's LLM API to perform general tasks similar to Alexa, Siri, or Google Assistant.

## Features

- **Voice Command Recognition**: Uses the `SpeechRecognition` library to listen and recognize user voice commands.
- **Web Automation**: Opens popular websites like Google, Facebook, YouTube, and LinkedIn upon command.
- **Music Playback**: Plays songs using URLs fetched from the `musicLibrary`.
- **Natural Language Processing**: Processes and answers queries using Groq LLM (`llava-v1.5-7b-4096-preview` model) for more complex tasks or general conversations.
- **Simple Commands**: Can be triggered with the wake word "Alexa" and responds with various tasks.

## Installation

1. Clone this repository to your local machine:

```bash
git clone https://github.com/VRAJ-07/Alexa-Voice-Assistant-Using-LLM.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Set your Groq API key:

```bash
export GROQ_API_KEY='your_groq_api_key'
```

## Dependencies

The assistant relies on the following Python libraries:

- `SpeechRecognition`: For voice recognition.
- `pyttsx3`: For text-to-speech conversion.
- `webbrowser`: To handle web automation.
- `langchain-core`: To create prompt templates and chains.
- `langchain-groq`: To use Groq's LLM for complex command handling.
- `musicLibrary.py`: Handles music playback by fetching song URLs.

## Usage

1. Run the main script:

```bash
python app.py
```

2. The assistant will initialize and listen for the wake word "Alexa." Once it recognizes the wake word, you can issue commands like:

- "Open Google"
- "Play [Song Name]"
- "Open YouTube"
- General questions or requests (handled by the Groq LLM)

3. To stop the program, simply say "stop."

## Example Commands

- **Opening websites**: 
  - "Open Google"
  - "Open YouTube"
- **Playing music**: 
  - "Play Animals"
- **General conversation**: 
  - "Tell me a joke"
  - "What's the weather like?"
