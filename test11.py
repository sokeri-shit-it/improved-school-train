import requests

get_forward_city = "https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Владивосток&format=json"
get_delivery_city = "https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Хабаровск&format=json"

for_responce, del_responce = requests.get(get_forward_city), requests.get(get_delivery_city)

if for_responce and del_responce:

    for_response_json, del_response_json = for_responce.json(), del_responce.json()

    toponym1 = for_response_json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    meta_coords1 = toponym1["metaDataProperty"]["GeocoderMetaData"]["text"]
    coords1 = toponym1["Point"]["pos"]

    toponym2 = del_response_json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    meta_coords2 = toponym2["metaDataProperty"]["GeocoderMetaData"]["text"]
    coords2 = toponym2["Point"]["pos"]

    api_server = "http://static-maps.yandex.ru/1.x/"

    lon = str((float(coords1.split(' ')[0]) + float(coords2.split(' ')[0])) / 2)
    lat = str((float(coords1.split(' ')[1]) + float(coords2.split(' ')[1])) / 2)
    delta = "10"

    params = {
        "ll": ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": "map"
    }
    response = requests.get(api_server, params=params)

map_file = "static/img/map.png"
with open(map_file, "wb") as file:
    file.write(response.content)