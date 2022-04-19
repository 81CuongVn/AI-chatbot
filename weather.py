from texttospeech import texttospeech 
import requests, json
# Python program to find current
# weather details of any city
# using openweathermap api

# import required module# Enter your API key here
def weather():

    api_key = "f5e58e5107262dd200ef30cc9e47355a"

    # base_url variable to store url
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name
    city_name = input("Enter city name : ")
    texttospeech("mời nhập tên thành phố")

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":

        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
        unit = current_temperature - 273.15 
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
        # print following values
        result = """thời tiết hiện thời của {city_name} là có nhiệt độ = {unit} áp suất không khí = {current_pressure} độ ẩm = {current_humidity}""".format(city_name = city_name, unit = unit, current_pressure = current_pressure, current_humidity = current_humidity)
        texttospeech(result)    
    else:
        texttospeech("thành phố không tồn tại")
