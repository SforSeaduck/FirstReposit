from pywebio.output import *
from pywebio.input import input as input_pw, select, slider, radio
from pywebio.session import set_env

username = input_pw("Введіть ваше ім'я:", type='text')
film_name = input_pw("Введіть назву фільму:", type='text')
genre = select('Виберіть жанр фільму:', options=['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi'])
review = input_pw('Напишіть короткий відгук про фільм:')
rating = slider("Встановіть рейтинг фільму (від 1 до 10):", min=1, max=10, step=1, value=5)
emotions = select("Виберіть ваші емоції після перегляду фільму:",
                  options=['Захоплення', 'Сміх', 'Враження', 'Страх', 'Розчарування'])
recommend = radio("Чи рекомендуєте ви цей фільм іншим?", options=['Так', 'Ні'])

reviews_info = [username, film_name, genre, review, rating, emotions, recommend]
if rating > 7:
    put_text("Ви дали високий рейтинг цьому фільму! Дякуємо за відгук!")

set_env(output_animation=True)
