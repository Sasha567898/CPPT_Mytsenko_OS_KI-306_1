package KI306.Mytsenko.Lab6;
/**
 * Class EquationsApp Implements driver for Equations class
 *
 * @author Oleksandr Mytsenko
 * @version 1.0
 */

public class Main {
    /**
     * The main method is the entry point of the program.
     *
     * @param args The command-line arguments (not used in this program).
     */
    public static void main(String[] args) {
        Penal <? super Item> penal = new Penal<>();
        penal.putItem(new Rubber("Rubber1", 10.50));
        penal.putItem(new Scissors("Scissors1" , 55.75));
        penal.putItem(new Rubber("Rubber2" , 15.25));
        penal.putItem(new Scissors("Scissors2" , 100));

        System.out.println(penal.getMax().getPrice());

       // Item item = penal.getItem(2);
        //item.print();

       //item = penal.getItem(3);
        //item.use();

        //Item max = penal.getMax();
      //  System.out.println("\nThe the most expensive item in penal is: ");
        //max.print();
    }
}
