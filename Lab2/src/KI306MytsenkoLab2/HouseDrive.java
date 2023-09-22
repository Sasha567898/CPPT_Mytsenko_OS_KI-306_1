package KI306MytsenkoLab2;

public class HouseDrive {
    public static void main(String[] args) {
        House house1 = new House("Вулиця Лінкольна, 123", 3, true);
        House house2 = new House("Вулиця Індепенденс, 456");
        House house3 = new House("Вулиця Кеннеді, 789", 2);

        house1.openLogFile();
        house2.openLogFile();
        house3.openLogFile();

        house1.displayDetails();
        house2.displayDetails();
        house3.displayDetails();

        house1.setAddress("Вулиця Нова, 555");
        house1.setNumberOfFloors(4);
        house1.addFloor();
        house1.setHasGarden(false);
        house1.removeFloor();

        house2.setNumberOfFloors(6);
        house2.addFloor();
        house2.setHasGarden(true);
        house2.removeFloor();

        house3.setHasGarden(true);
        house3.addFloor();

        house1.displayDetails();
        house2.displayDetails();
        house3.displayDetails();

        house1.closeLogFile();
        house2.closeLogFile();
        house3.closeLogFile();
    }
}
