
import java.util.Scanner;
public class marks {
    public static void main(String[] args) {
        Scanner sn = new Scanner(System.in);
        System.out.println("Enter the marks for 5 subs");
        System.out.println("Enter the marks for Subject 1 : ");
        int sub1 = sn.nextInt();
        System.out.println("Enter the marks for Subject 2 : ");
        int sub2 = sn.nextInt();
        System.out.println("Enter the marks for Subject 3 : ");
        int sub3 = sn.nextInt();
        System.out.println("Enter the marks for Subject 4 : ");
        int sub4 = sn.nextInt();
        System.out.println("Enter the marks for Subject 5 : ");
        int sub5 = sn.nextInt();
        sn.close();
        int sum = sub1+sub2+sub3+sub4+sub5;

        System.out.print("The Total Marks is : ");
        System.out.print(sum);
        System.out.println("/500");
        

    }
}

