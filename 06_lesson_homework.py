from pywebio.output import *
from pywebio.input import input as input_pw

put_html("<h1>УРА, ЛІТО!</h1>")

poem = """
    Літо прийшло, сонечко сміється,
    Пташки співають, квіти цвітуть.
    Відпочиваймо, весело трішки,
    Щоб кожен день нас щасливим зробить! 😊
    """
put_text(poem)

plans = input_pw('Введiть вашi плани на лiто:')

plan_symbol_counter = len(plans.strip())
put_text(f"У ваших планах на літо {plan_symbol_counter} символів")

put_image("https://www.wfla.com/wp-content/uploads/sites/71/2023/05/GettyImages-1389862392.jpg?w=2560&h=1440&crop=1")
