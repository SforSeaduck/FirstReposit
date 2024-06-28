import requests
from pprint import pprint

url = 'https://dummyjson.com/users'

response = requests.get(url)
#pprint(response.json())
dict_with_users = response.json()
list_of_users = dict_with_users['users']
count_of_users = dict_with_users['total']
for counter in range (0, count_of_users):
    if list_of_users[counter]['age'] == 28:
        print(list_of_users[counter]['firstName'])