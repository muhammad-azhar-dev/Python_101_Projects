weather = {
    "coord":
    {"lon":-0.1257,"lat":51.5085},
    "weather":
    [{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04n"}],
    "base":"stations",
    "main":{"temp":6.59,"feels_like":5.16,"temp_min":5.28,"temp_max":7.29,"pressure":1034,"humidity":95,"sea_level":1034,"grnd_level":1029},
    "visibility":8000,
    "wind": {"speed":2.06,"deg":180},
    "clouds":{"all":100},
    "dt":1737006911,
    "sys":{"type":2,"id":2075535,"country":"GB","sunrise":1737014304,"sunset":1737044504},
    "timezone":0,
    "id":2643743,
    "name":"London",
    "cod":200
    
}
print(weather['cod'])