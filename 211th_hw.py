def calculate_discounted_price(price, discount):

    if price < 0:
        raise ValueError("Ціна не може бути меншою за 0.")
    if discount < 0 or discount > 100:
        raise ValueError("Відсоток знижки має бути між 0 і 100.")

    return price * (1 - discount / 100)

def test_calculate_discounted_price():
    assert calculate_discounted_price(100, 10) == 90
    assert calculate_discounted_price(200, 25) == 150
    assert calculate_discounted_price(50, 0) == 50
    assert calculate_discounted_price(100, 100) == 0
    try:
        calculate_discounted_price(-10, 10)
    except ValueError as e:
        assert str(e) == "Ціна не може бути меншою за 0."
    try:
        calculate_discounted_price(100, 110)
    except ValueError as e:
        assert str(e) == "Відсоток знижки має бути між 0 і 100."
    try:
        calculate_discounted_price(100, -10)
    except ValueError as e:
        assert str(e) == "Відсоток знижки має бути між 0 і 100."

test_calculate_discounted_price()
