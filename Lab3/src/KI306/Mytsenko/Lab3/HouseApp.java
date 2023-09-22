package KI306.Mytsenko.Lab3;

/**
 * The {@code HouseDriver} class provides a simple driver program to test the House and OfficeCenter classes.
 *
 * @author Your Name
 * @version 1.0
 */
public class HouseApp {
    public static void main(String[] args) {
        // Create an office center
        OfficeCenter officeCenter = new OfficeCenter("789 Oak St.", 5, 500, true, 50, true, true);

        // Display office center details
        officeCenter.displayDetails();

        // Update office center details
        officeCenter.setNumberOfFloors(6);
        officeCenter.setAddress("101 Pine St.");
        officeCenter.setOfficeSpace(600);
        officeCenter.equipMeetingRoom(false, true);
        officeCenter.addDesks(10);

        // Display updated office center details
        officeCenter.displayDetails();
    }
}
