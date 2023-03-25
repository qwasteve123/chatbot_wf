from rsc import *
import subprocess


if __name__ == "__main__":
    
    #start programs by bat file
    subprocess.Popen(".\start_app.bat")

  # enter api_key for openai module for chatgpt
    gpt = Chatgpt(api_key=api_key,dialogue=dialogue,model=model)

    # set OPENAI_API_KEY in environment variablesy
    gpt.set_env_var()
    res_content = gpt.conversation()
    while True:
        # Speak and print response
        print(f'Response: {res_content}')
        print("#####################")
        speak(res_content)

        # record audio input
        # recording will be saved in src file : output.wav
        record_sound(event_key = 'esc')

        # Whisper module takes output.wav to speech
        #audio user speech and return text
        question = speech_to_text_api()
        print(f'User: {question}')
        question = speech_to_text_api() + '日本語で答えてください。'
        # question = question + ', please answer in short.'

        # If speak 'Exit', pretending user saying goodbye in chatgpt
        if 'exit' in question or 'Exit' in question:
            res_content = gpt.conversation('さようなら')
            break

        # After recive user speech text, return response
        res_content = gpt.conversation(question)

    # Session ended, final response from chatgpt
    print(f'Response: {res_content}')
    speak(res_content)
    
    #
    gpt.remove_env_var()

    #start programs by bat file
    subprocess.Popen(".\close_app.bat")
