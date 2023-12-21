from datetime import datetime

class House:
    def __init__(self, address="No information", number_of_floors=0, has_garden=False):
        self.address = address
        self.number_of_floors = number_of_floors
        self.has_garden = has_garden

    def display_details(self):
        print(f"Адреса будинку: {self.address}")
        print(f"Кількість поверхів: {self.number_of_floors}")
        print(f"Наявність саду: {'Так' if self.has_garden else 'Ні'}")

    def set_number_of_floors(self, number_of_floors):
        self.number_of_floors = number_of_floors
       # self.log_message(f"Встановлено кількість поверхів: {number_of_floors}")

    def set_address(self, address):
        self.address = address
      #  self.log_message(f"Оновлено адресу: {address}")

    def set_has_garden(self, has_garden):
        self.has_garden = has_garden
      #  self.log_message("Оновлено інформацію про сад.")

    def add_floor(self):
        self.number_of_floors += 1
       # self.log_message("Додано поверх.")

    def remove_floor(self):
        if self.number_of_floors > 0:
            self.number_of_floors -= 1
            #self.log_message("Видалено поверх.")

         # self.log_message("Не можна видалити поверх. Кількість поверхів вже мінімальна.")

    def get_number_of_floors(self):
      #  self.log_message("Дана інформація про кількість поверхів.")
        return self.number_of_floors

    def get_address(self):
        #self.log_message("Дана інформація про адресу.")
        return self.address

    def has_garden_info(self):
       # self.log_message("Дана інформація про наявність саду.")
        return self.has_garden



# Приклад використання класу
if __name__ == "__main__":
    house = House("Some address1", 2, True)

    house.display_details()
    house.set_number_of_floors(3)
    house.set_address("New address")
    house.add_floor()
    house.remove_floor()

    print(f"Кількість поверхів: {house.get_number_of_floors()}")
    print(f"Адреса будинку: {house.get_address()}")
    print(f"Наявність саду: {house.has_garden_info()}")

    del house  # закриття файлу перед знищенням об'єкту
