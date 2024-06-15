ticket_cost = 500
taxi_to_park_cost = 600
taxi_from_park_cost = taxi_to_park_cost * 1.2
count_of_pizza = 2
pizza_cost = 250
pizza_cost_in_all = pizza_cost * count_of_pizza
pizza_cost_in_all_with_loto = pizza_cost_in_all * 0.85
air_hockey_cost = 80
air_hokey_games_played = 8
air_hokey_cost_in_all = air_hockey_cost * air_hokey_games_played
number_of_people = 4

total_cost = ticket_cost * number_of_people + taxi_to_park_cost + taxi_from_park_cost + pizza_cost_in_all_with_loto + air_hokey_cost_in_all
money_per_people = total_cost / number_of_people

print('Кожен друг мусить заплатити по ', money_per_people,'гривень')


