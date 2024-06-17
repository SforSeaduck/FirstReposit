header = '~' * 50
footer = header
symbol = '*' * 10
print(header)
print(header)
dish_name = input('Enter dish name: ')
recipe = input('Enter a recipe name what you like: ')
counter_of_meat = recipe.count('meat')

modded_dish_name = dish_name.strip().upper()
modded_recipe = recipe.strip().lower()

print(symbol, modded_dish_name, symbol)
print(modded_recipe, '😋😋😋😋')

print(f'count of words "meat" = ', {counter_of_meat})
print(footer)