import requests
from pprint import pprint
url = 'https://dummyjson.com/todos'

params = {
    'limit': 100,
    'skip': 0,
}
def ge_todos(limit: int = 50, skip: int = 0) -> dict:
    response = requests.get(url= url, params=params)
    response.request.get()

"""
import requests
from pprint import pprint


url = 'https://dummyjson.com/todos'

# response = requests.get(url=url, params=params)
#
# # print(response)
# # print(response.content)
# # print(response.text)
# response_json = response.json()
# todos = response_json['todos']


def get_todos(limit: int = 50, start: int = 0) -> list[dict]:
    params = {
        'limit': limit,
        'skip': start,
    }
    response = requests.get(url=url, params=params)
    response_json = response.json()
    todos = response_json['todos']
    return todos

def get_completed_todos_number(todos_candidates: list[dict], is_completed: bool = True) -> int:
    counter = 0
    for todo in todos_candidates:

        if todo['completed'] is is_completed:
            counter += 1
    return counter


start = 0
limit = 50
has_next = True
for iterator in range(1, 301):
    chunk = get_todos(start=start, limit=limit)
    start += limit
    print(chunk)
"""

"""
def get_todos_by_content(todos_candidates: list[dict], content: str) -> list[str]:
    content_list = []
    for todo in todos_candidates:
        if content.lower() in todo["todo"].lower():
            content_list.append(todo["todo"])

    return content_list


start = 0
limit = 50

completed_successfully = 0
completed_unsuccessfully = 0
content_lst = []
content_word = 'solve'
for iterator in range(1, 301):
    chunk = get_todos(start=start, limit=limit)
    if not chunk:
        break
    completed_successfully += get_completed_todos_number(chunk)
    completed_unsuccessfully += get_completed_todos_number(chunk, is_completed=False)
    content_lst += get_todos_by_content(chunk, content_word)
    start += limit

print(f'{completed_successfully=}, {completed_unsuccessfully=} {2+2=}')
pprint(content_lst) 
"""