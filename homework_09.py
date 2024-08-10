from pywebio import start_server
from pywebio.input import input, select, textarea, slider, radio
from pywebio.output import put_text, put_markdown, put_buttons, clear
import time

reviews_info = []

def main():

    name = input("Введіть ваше ім'я:", type="text")
    movie_title = input("Введіть назву фільму:", type="text")
    genre = select("Виберіть жанр фільму:", options=["Бойовик", "Комедія", "Екшн", "Жахи", "Триллер", "horror"])
    review = textarea("Введіть короткий відгук про фільм:")
    rating = slider("Оцініть фільм від 1 до 10:", min_value=1, max_value=10)
    emotions = select("Які ваші емоції після перегляду фільму?", options=["Задоволений", "Розчарований", "Вражений", "Здивований"])
    recommend = radio("Чи рекомендуєте ви цей фільм іншим?", options=["Так", "Ні"])

    reviews_info.append({
        "name": name,
        "movie_title": movie_title,
        "genre": genre,
        "review": review,
        "rating": rating,
        "emotions": emotions,
        "recommend": recommend
    })

    if rating >= 8:
        put_text(f"Дякуємо за ваш відгук, {name}! Ваша оцінка фільму '{movie_title}' дуже висока!")
    else:
        put_text(f"Дякуємо за ваш відгук, {name}! Ваша оцінка фільму '{movie_title}'")

    time.sleep(4)
    clear()

if __name__ == '__main__':
    start_server(main, port=8080)
