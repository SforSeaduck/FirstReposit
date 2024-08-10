import requests 
import json

pdf_url = 'https://chtyvo.org.ua/authors/Falkovych_Hryhorii/Smyk-tyndyk.pdf'
pdf_response = requests.get(pdf_url)

if pdf_response.status_code == 200:
    with open('Smyk-tyndyk.pdf', 'wb') as file:
        file.write(pdf_response.content)
    print('PDF файл завантажено успішно!')
else:
    print(f'Не вдалося завантажити PDF файл. Статус коду: {pdf_response.status_code}')


