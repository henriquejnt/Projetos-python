"""Site da API: https://console.hgbrasil.com/documentation/weather/tools"""
import requests
import json
nome_cidade = input('Nome da cidade brasileira: ')
dados_climaticos = (requests.get(f'https://api.hgbrasil.com/weather?key=SUA-CHAVE&city_name={nome_cidade}')).json()

hora_última_atualização = dados_climaticos['results']

data_atual = dados_climaticos['results']

umidade = dados_climaticos['results']

cidade = dados_climaticos['results']

#pega chuva
probabilidade_chuva = dados_climaticos['results']['forecast']
probld_chuva = next(item['rain_probability'] for item in probabilidade_chuva if item['date'])

nebulosidade = dados_climaticos['results']
velocidade_vento = dados_climaticos['results']
tempo = dados_climaticos['results']

#pega temperatura maxima
maxima = dados_climaticos['results']['forecast']
max_dia_30 = next(item['max'] for item in maxima if item['date'])
minima = dados_climaticos['results']

#pega temperatura minima
minima = dados_climaticos['results']['forecast']
temp_minima = next(item['min'] for item in minima if item['date'])

#pega a condição
cond = dados_climaticos['results']['forecast']
condicao = next(item['description'] for item in cond if item['date'])

#imprime os dados
print('Cidade: ', cidade['city'])
print('Dia atual: ', data_atual['date'])
print('Hora da última atualização: ',hora_última_atualização['time'])
print('Umidade: ', umidade['humidity'],'%')
print('Nebulosidade: ', nebulosidade['cloudiness'],'%')
print('Velocidade do vento: ',velocidade_vento['wind_speedy'])
print('Temperatura atual: ',tempo['temp'],'°')
print('Temperatura máxima registrada: ', max_dia_30,'°')
print('Temperatura miníma registrada: ',temp_minima,'°')
print('Probabilidade de chuva: ',probld_chuva,'%')
print('Condição: ',condicao)
