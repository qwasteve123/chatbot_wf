
import requests, json
import io
import wave
import pyaudio
import time
import re
import threading

class Voicevox:
    def __init__(self,host="127.0.0.1",port=50021):
        self.host = host
        self.port = port
        self.audio_list = [None]

    def speak(self,text=None,speaker=48,split=True): # VOICEVOX character
        # split recived paragraph to shorter sentences.
        if split:
            sentences = to_list(text)
            if not sentences:
                raise Exception("No text.")
        else:
            sentences = [text]
        
        # fill whole list with None to create the length of the list of audio
        self.audio_list = [None for i in range(len(sentences))]  

        #Threading inside multi_read function. each sentence created an audio for sentence list.
        #PRevent loading whole paragraph
        # Help reduce waiting time for voice ouput
        def multi_read():
            t_list = []

            # generating audio for 3 sentences for each iteration.
            for i in range(0,len(sentences),3):
                # check the last round iteration if less then 3 run the sentences left.
                k = len(sentences) - i if i+3 > len(sentences) else 3
                #set up threading
                for j in range(0,k):
                    t = threading.Thread(target=self.text_to_audio,args=(sentences[i+j],speaker,i+j))
                    t_list.append(t)
                for t in t_list:
                    t.start()
                for t in t_list:
                    t.join()
                t_list = []

        # Multithreading of generating audio and playing audio simutaneously.
        def multi_play():
            # run all audio
            for i in range(len(sentences)):
                # Wait until the first audio is in the list
                while not self.audio_list[i]:
                    pass
                self.play_audio(self.audio_list[i])

        # Multithreading both read audio and playing audio
        t_1 = threading.Thread(target=multi_read)
        t_2 = threading.Thread(target=multi_play)
        t_1.start()
        t_2.start()
        t_1.join()
        t_2.join()

        # clear audio list
        self.audio_list = []

    def temp_speak(self,text=None,speaker=48):
        audio = self.text_to_audio(text,speaker)
        self.play_audio(audio)

    def text_to_audio(self,text,speaker,thread_seq=0):
        params = (
            ("text", text),
            ("speaker", speaker)  # 音声の種類をInt型で指定
        )

        init_q = requests.post(
            f"http://{self.host}:{self.port}/audio_query",
            params=params
        )

        res = requests.post(
            f"http://{self.host}:{self.port}/synthesis",
            headers={"Content-Type": "application/json"},
            params=params,
            data=json.dumps(init_q.json())
        )

        # メモリ上で展開
        audio = io.BytesIO(res.content)

        self.audio_list[thread_seq] = audio

        return audio

    def play_audio(self,audio=None):
        with wave.open(audio,'rb') as f:
            # 以下再生用処理
            p = pyaudio.PyAudio()

            def _callback(in_data, frame_count, time_info, status):
                data = f.readframes(frame_count)
                return (data, pyaudio.paContinue)

            output_device_index = 8
            for i in range(p.get_device_count()):
                if 'CABLE Input (VB-Audio Virtual Cable)' == p.get_device_info_by_index(i):
                    output_device_index = i
            stream = p.open(format=p.get_format_from_width(width=f.getsampwidth()),
                            channels=f.getnchannels(),
                            rate=f.getframerate(),
                            output=True,
                            # Set output device to virtual cable
                            output_device_index=output_device_index,
                            stream_callback=_callback)

            # Voice再生
            stream.start_stream()
            while stream.is_active():
                time.sleep(0.01)

            stream.stop_stream()
            stream.close()
            p.terminate()

def speak(text):
    speaker = 4
    vv = Voicevox()
    vv.speak(text=text,split=True,speaker=speaker)

def to_list(text):
    # to keep the punctuation of sentence to fix the pronunciation of "は" in "wa" not "ha"
    sentences = []
    whole_word = True
    start_pointer = 0
    symbol = "。|! |？"
    for index, char in enumerate(text):
        if char in symbol:
            sentence = text[start_pointer:index+1]
            start_pointer = index+1
            sentences.append(sentence)
            whole_world = False
    if whole_word:
        sentences.append(text)
    return sentences

    # sentences = re.split(symbol,text)
    # if sentences[-1] == "":
    #     return re.split(symbol,text)[:-1]
    # else:
    #     return re.split(symbol,text)

if __name__ == "__main__":

    # paragraph = ""
    # txt = open('./audio_test/test_audio.txt',encoding='utf8')
    # for line in txt:
        # paragraph = paragraph + line
    # paragraph = "簡単に言えば、「お待ちしました。」は反省を表し、謙虚な表現、「お待ちどうさま。」は感謝の気持ちを表し、客に対する気遣いを表します。ただし、このような微妙なニュアンスの違いは、地域や店舗によっても異なる場合があるので、 一概には言えません。"
    paragraph= "jump"
    speak(paragraph)