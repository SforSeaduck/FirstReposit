class Car:
    def __init__(self, manufacturer, model, fuel_consumption, year=2020, mileage=0):
        self.year = year
        self.manufacturer = manufacturer
        self.model = model
        self.mileage = mileage
        self.fuel_consumption = fuel_consumption

    def __str__(self):
        return (f"Автомобіль {self.manufacturer} {self.model} ({self.year})\n"
                f"Пробіг: {self.mileage} км\n"
                f"Витрата палива: {self.fuel_consumption} л/100 км")

car_1 = Car(manufacturer="Nissan", model="Leaf", fuel_consumption='62kW AT')
car_2 = Car(manufacturer="Audi", model="Q7", fuel_consumption=3.0,)
car_3 = Car(manufacturer="LEXUS", model="RX", fuel_consumption=2.99)

print(car_1)
print(car_2)
print(car_3)
