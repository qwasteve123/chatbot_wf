import pyaudio
import wave
import time
import keyboard

# return a pyaudio.stream object
def record_sound(event_key ='esc'):

    # Set the parameters for the recording
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "output.wav"

    # Create an instance of the PyAudio class
    audio = pyaudio.PyAudio()

    # Open the microphone and start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Recording started...")

    frames = []

    # Record for the specified number of seconds
    # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    #     data = stream.read(CHUNK)
    #     frames.append(data)
    # recording = False
    while True:
        if keyboard.is_pressed(event_key):
            print('Recording')
            start_time = time.time()
            break
    while True:
        if keyboard.is_pressed(event_key):
            data = stream.read(CHUNK)
            frames.append(data)  
        else:
            break    
    end_time = time.time()
    print(end_time-start_time," seconds")



    print("Recording stopped.")

    # Stop the recording and close the microphone
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio as a WAV file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print("Audio saved to " + WAVE_OUTPUT_FILENAME)

if __name__ == "__main__":
    record_sound('esc')

