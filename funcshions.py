from pywebio.output import *
from pywebio.input import input as input_pw

def html_headers_creator(username):

    username = input_pw('Як вас звати?')
    html_header = f"<h1>Вітаємо тебе шановний, {username}</h1>"
    put_html(f"<h1>{html_header}</h1>")

    return html_header

html_headers_creator('username')
