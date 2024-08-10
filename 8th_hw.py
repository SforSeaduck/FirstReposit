from pywebio import start_server
from pywebio.input import input, select, slider, NUMBER
from pywebio.output import put_text, put_image, clear

def quiz():
    total_score = 0

    name = input("Введіть ваше ім'я:", type="text")

    questions = [
        {
            'question': 'Яка столиця Східної Римської імперії?',
            'answer': 'Константинополь',
            'type': 'text'
        },
        {
            'question': 'Коли вибухнула ЧАЕС?',
            'answer': 1986,
            'type': 'number'
        },
        {
            'question': 'Скільки континентів на Землі?',
            'answer': 7,
            'type': 'number'
        },
        {
            'question': 'Яка найбільша планета в нашій сонячній системі?',
            'answer': 'Юпітер',
            'type': 'text'
        },
        {
            'question': 'Хто був першим президентом США?',
            'answer': 'Джордж Вашингтон',
            'type': 'text'
        }
    ]

    for q in questions:
        if q['type'] == 'text':
            response = input(q['question'], type="text").strip().lower()
        elif q['type'] == 'number':
            response = input(q['question'], type=NUMBER)
        else:
            response = None

        if response == q['answer']:
            total_score += 1

    put_text(f"Дякуємо за проходження вікторини, {name}!")
    put_text(f"Ваш бал: {total_score} з 5")

    if total_score == 5:
         put_image('C:\\Users\\vasyl\\Desktop\\FirstReposit\\images.jpg')


    import time
    time.sleep(4)
    clear()

if __name__ == '__main__':
    start_server(quiz, port=8080)
