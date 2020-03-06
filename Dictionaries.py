meteo = {
    'city': 'Москва',
    'temperature': '20'
}
meteo['temperature'] = int(meteo['temperature'])-5
print(meteo)
print(meteo.get('countre'))
print(meteo.get('countre', 'RF'))
meteo['date'] = '27.02.2020'
print(meteo)
print(len(meteo))
