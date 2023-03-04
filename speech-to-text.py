import openai
import os

openai.api_key = os.environ['API_KEY']

def convert_speech_to_text(audio):
    audio_file= open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript