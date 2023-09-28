import java.util.Scanner;

public class inPut {
    public static void main(String[] args) {
        System.out.println("Taking input from user");
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number 1: ");
        int a = sc.nextInt();
        System.out.println("Enter number 2: ");
        int b = sc.nextInt();
        int sum = a+b;
        System.out.print("The sum of these no.s is : ");
        System.out.println(sum);
        sc.close();
    }
}
