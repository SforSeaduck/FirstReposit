import requests
import json

api_url = 'http://api.open-notify.org/astros.json'
api_response = requests.get(api_url)

if api_response.status_code == 200:
    data = api_response.json()
    
    with open('astros.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print('Дані з API записані у JSON файл успішно!')
else:
    print(f'Не вдалося отримати дані з API. Статус код: {api_response.status_code}')