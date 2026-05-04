import requests

# Contexto: consulta de meteorologia atual para o Porto
latitude = 41.1579
longitude = -8.6291

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

resposta = requests.get(url)
dados = resposta.json()

temperatura = dados["current_weather"]["temperature"]
vento = dados["current_weather"]["windspeed"]

print("Dados meteorológicos atuais - Porto")
print(f"Temperatura: {temperatura} °C")
print(f"Velocidade do vento: {vento} km/h")