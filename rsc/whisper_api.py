import whisper
import time


class get_whisper():
    def __init__(self):
        self.model = whisper.load_model('small',) 

    def speech_to_text(self,input_file="output.wav"):
        result = self.model.transcribe(input_file,fp16=False)
        return result["text"]
    
def speech_to_text(input_file="output.wav"):
    g = get_whisper()
    text = g.speech_to_text(input_file=input_file)
    return text

if __name__ == "__main__":
    print(speech_to_text(input_file="audio.mp3"))