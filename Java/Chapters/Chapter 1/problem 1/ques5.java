import java.util.Scanner;

public class ques5 {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("The Enter Something : ");
        if (sc.hasNextInt()){
            System.out.println("The Entered Number is a INT");
        }
        else if (sc.hasNextFloat()){
            System.out.println("The Number entered is a Float");
        }
        else {
            System.out.println("The Number entered is a String");
        }

        sc.close();
    }
}
