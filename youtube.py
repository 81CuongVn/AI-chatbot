from texttospeech import texttospeech
from youtubesearchpython import VideosSearch
def youtube():
    texttospeech("nhập tên video để tìm kiếm trên youtube")
    url = input("nhap de tim video tren youtube: ")
    videosSearch = VideosSearch(url, limit = 2)
    print(videosSearch.result())
    texttospeech("đây là các kết quả tìm kiếm")