import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

test_filename = "test.wav"
filename_from_mic = "Recording.wav"
voice_text_filename = "voice_as_text.txt"

r = sr.Recognizer()

def recognize_from_file(filename):
    with sr.AudioFile(filename) as source:  
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data)  
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            text = ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            text = ""
        return text

def recognize_from_mic(file_to_write):
    sample_rate = 44100
    duration = 5
    print("Recording audio")
    audio_recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    print("Recording complete")
    wav.write(file_to_write, sample_rate, audio_recording)

def save_text_to_file(text, filename):
    with open(filename, 'w') as f:
        f.write(text)

if __name__ == "__main__":
    print(recognize_from_file(test_filename))
    recognize_from_mic(filename_from_mic)
    text_from_voice = recognize_from_file(filename_from_mic)
    save_text_to_file(text_from_voice, voice_text_filename)
