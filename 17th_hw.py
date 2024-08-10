def result_as_dict_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return {'result': result}
    return wrapper

@result_as_dict_decorator
def multiply(a, b):
    return a * b

print(multiply(7, 444231))
