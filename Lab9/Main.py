from house import House
from office_center import OfficeCenter

# Код для тестування класів House і OfficeCenter
if __name__ == "__main__":
    house = House("Lazarenka", 2, True)

    house.display_details()
    house.set_number_of_floors(3)
    house.set_address("New address")
    house.add_floor()
    house.remove_floor()

    print(f"Кількість поверхів: {house.get_number_of_floors()}")
    print(f"Адреса будинку: {house.get_address()}")
    print(f"Наявність саду: {house.has_garden_info()}")

    del house  # закриття файлу перед знищенням об'єкту

    office = OfficeCenter("Central", 3, 500, True, 50, True, True)
    #office.display_details()

    office.set_office_space(600)
    office.allocate_office_space(100)
    office.equip_meeting_room(True, False)
    office.add_desks(10)
    office.remove_desks(5)
    office.add_projector(True)
    office.add_whiteboard(False)

    #office.display_details()