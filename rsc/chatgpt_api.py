import openai
import os



class Chatgpt(): 
    def __init__(self,api_key=None,dialogue=[],model="gpt-3.5-turbo"):
        self.api_key = api_key
        self.dialogue = dialogue  
        self.model = model      

    # remove api key environment variables
    def remove_env_var(self):
        os.environ.pop('OPENAI_API_KEY',None)

    def set_env_var(self):
        os.environ['OPENAI_API_KEY'] = self.api_key
        openai.api_key = os.environ['OPENAI_API_KEY']

    # 
    def conversation(self,question="") -> str:
        if question:
            self.dialogue.append({"role": "user","content":question})
        response = openai.ChatCompletion.create(model=self.model,messages=self.dialogue )
        reply = response["choices"][0]["message"]["content"]
        self.dialogue.append(response["choices"][0]["message"])
        return reply

if __name__ == "__main__":

    model= "gpt-3.5-turbo"
    dialogue = [{"role":"system","content":"You are an AI assistant"},
                {"role": "user","content":"Hi"},]
    api_key = "..."



if __name__ == "__main__":
    # enter api_key for openai module for chatgpt
    gpt = Chatgpt(api_key=api_key,dialogue=dialogue,model=model)

    # set OPENAI_API_KEY in environment variablesy
    gpt.set_env_var()
    res_content = gpt.conversation()
    while True:
        # Speak and print response
        print(f'Response: {res_content}')
        print("#####################")

        question=input()
        print(f'User: {question}')

        # If speak 'Exit', pretending user saying goodbye in chatgpt
        if 'Exit' in question:
            break

        # After recive user speech text, return response
        res_content = gpt.conversation(question)

    # Session ended, final response from chatgpt
    print(f'Response: {res_content}')

    
    #
    gpt.remove_env_var()