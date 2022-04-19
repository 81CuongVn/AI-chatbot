import speech_recognition as sr
import pyaudio

def speechtotext():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Mời bạn nói: ")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language="vi-VI")
            print("Bạn -->: {}".format(text))
        except:
            print("Xin lỗi! tôi không nhận được voice!")
    return text