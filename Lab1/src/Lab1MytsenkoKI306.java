import java.io.*;
import java.util.*;


public class Lab1MytsenkoKI306 {

    public static void main(String[] args) throws FileNotFoundException {
        System.out.print("Введіть розмір квадратної матриці: ");
        Scanner in = new Scanner(System.in);
        int nRows = in.nextInt();
        System.out.print("Введіть символ-заповнювач: ");
        in.nextLine();
        String filler = in.nextLine();
        if (filler.length() != 1)
        {
            System.out.print("\nСимвол-заповнювач введено невірно.");
            System.exit(0);
        }
        char[][] arr = new char[nRows][];

        PrintWriter wFile = new PrintWriter ("MyFile.txt");

        for (int I = 0; I < nRows; I++)
        {
            for (int K = nRows; K > I; K--) {
                System.out.print("\t");
                wFile.write("\t");
            }

            arr[I] = new char[I];
            for (int J = 0; J < I; J++)
            {
                arr[I][J] = (char)filler.codePointAt(0);
                System.out.print(arr[I][J] + "\t");
                wFile.write(arr[I][J] + "\t");
            }
            System.out.print("\n");
            wFile.print("\n");

        }
        wFile.close();
        in.close();
    }
}