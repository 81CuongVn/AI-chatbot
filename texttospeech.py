from gtts import gTTS
import playsound
import os 

# text = "tôi có thể giúp gì cho bạn" 
def texttospeech(text):
    output = gTTS(text,lang="vi", slow=False)
    output.save("output.mp3")
    playsound.playsound('output.mp3')
    os.remove("output.mp3")