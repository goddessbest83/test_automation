import requests
import pymongo
import datetime


openweather_seoul_url='https://api.openweathermap.org/data/2.5/weather?id=1835847&appid='
openweather_busan_url='https://api.openweathermap.org/data/2.5/weather?id=1838524&appid='
openweather_token = '{{openweather_token}}'

openweather_target_seoul_url = openweather_seoul_url+openweather_token
openweather_target_busan_url = openweather_busan_url+openweather_token

# response = requests.get(naver_url, headers = header_params)
response_seoul = requests.get(openweather_target_seoul_url)
response_busan = requests.get(openweather_target_busan_url)


response_seoul_json = response_seoul.json()
response_busan_json = response_busan.json()

now_time = datetime.datetime.now()
seoul_weather = response_seoul_json['weather'][0]['main']
seoul_Temperature = float(response_seoul_json['main']['temp']) - 273
seoul_Temperature = round(seoul_Temperature, 1)
seoul_city = response_seoul_json['name']
seoul_windspeed = float(response_seoul_json['wind']['speed'])

busan_weather = response_busan_json['weather'][0]['main']
busan_Temperature = float(response_busan_json['main']['temp']) - 273
busan_Temperature = round(busan_Temperature, 1)
busan_city = response_busan_json['name']
busan_windspeed = float(response_busan_json['wind']['speed'])

# connect mongo db
uri = '{{mongoDB_cluster_uri}}'
connection = pymongo.MongoClient(uri)
db = connection['weather_crawling']
collection = db['openweathermap']

seoul_post = { 'datetime': now_time, 'weather': seoul_weather, 'temperature': seoul_Temperature, 'city': seoul_city, 'windspeed': seoul_windspeed }
busan_post = { 'datetime': now_time, 'weather': busan_weather, 'temperature': busan_Temperature, 'city': busan_city, 'windspeed': busan_windspeed }

collection.insert_one(seoul_post)
collection.insert_one(busan_post)

connection.close()

print('Done')