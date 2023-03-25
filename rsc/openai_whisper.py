# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai
import os

def set_env_var():
    os.environ['OPENAI_API_KEY'] = "..."
    openai.api_key = os.environ['OPENAI_API_KEY']


def speech_to_text_api():
    set_env_var()
    audio_file= open("output.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return(transcript['text'])
