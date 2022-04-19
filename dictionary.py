import wikipedia
from texttospeech import texttospeech
def dictionary():
	texttospeech("nhập thứ bạn cần tìm kiếm trong từ điển")
	search = input("nhập thứ bạn cần tìm kiếm trên wikipedia: ")
	wikipedia.set_lang("vi")
	result = wikipedia.summary(search, sentences=4)
	texttospeech(result)