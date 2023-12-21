from house import House
class OfficeCenter(House):
    def __init__(self, address, number_of_floors, office_space,
                 has_meeting_room, number_of_desks, has_projector, has_whiteboard):
        super().__init__(address, number_of_floors)
        self.office_space = office_space
        self.has_meeting_room = has_meeting_room
        self.number_of_desks = number_of_desks
        self.has_projector = has_projector
        self.has_whiteboard = has_whiteboard

    def get_office_space(self):
        return self.office_space

    def set_office_space(self, office_space):
        self.office_space = office_space

    def allocate_office_space(self, square_meters):
        self.office_space += square_meters

    def equip_meeting_room(self, projector, whiteboard):
        self.has_meeting_room = True
        self.has_projector = projector
        self.has_whiteboard = whiteboard

    def add_desks(self, desks_to_add):
        self.number_of_desks += desks_to_add

    def remove_desks(self, desks_to_remove):
        if desks_to_remove > self.number_of_desks:
            print("Cannot remove more desks than available.")
        else:
            self.number_of_desks -= desks_to_remove

    def add_projector(self, has_projector):
        self.has_projector = has_projector
        # Additional logic related to adding a projector

    def add_whiteboard(self, has_whiteboard):
        self.has_whiteboard = has_whiteboard
        # Additional logic related to adding a whiteboard

    def display_details(self):
        print("Адреса офісного центру:", self.address)
        print("Кількість поверхів:", self.number_of_floors)
        print("Офісний простір (в м²):", self.office_space)
        print("Наявність зала для зустрічей:", "Так" if self.has_meeting_room else "Ні")
        print("Кількість робочих місць:", self.number_of_desks)
        print("Наявність проектора:", "Так" if self.has_projector else "Ні")
        print("Наявність дошки:", "Так" if self.has_whiteboard else "Ні")

    def __str__(self):
        return f"OfficeCenter: {self.address}, {self.number_of_floors} floors"

# Приклад використання класу
if __name__ == "__main__":
    office = OfficeCenter("Some address", 3, 500, True, 50, True, True)
    office.display_details()

    office.set_office_space(600)
    office.allocate_office_space(100)
    office.equip_meeting_room(True, False)
    office.add_desks(10)
    office.remove_desks(5)
    office.add_projector(True)
    office.add_whiteboard(False)

    office.display_details()
