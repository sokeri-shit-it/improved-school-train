from pyowm import owm
from pyowm.owm import OWM

city = input()
owm = OWM('9f2afc45adf2d8fd102136ea844b0348')
manager = owm.weather_manager()
observasion = manager.weather_at_place(city)
w = observasion.weather
temp = w.temperature('celsius')
normal_temp = temp['temp']
temp_feels = temp['feels_like']

wins = w.wind()['speed'] # скорость ветра

hum = w.humidity # влажность

clouds = w.clouds # облака

status = w.status # статус

print(normal_temp, wins, hum, clouds, status)
