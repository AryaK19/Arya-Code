import java.util.Scanner;

public class IfElse{
    public static void main(String[] args){
        // int age;
        // System.out.print("Enter Your age : ");
        // Scanner sc = new Scanner(System.in);

        // age = sc.nextInt();
        // sc.close();
        // switch(age){

        //     case 18 :
        //         System.out.println("You are going to become an Adult");
        //         break;
        //     case 23 :
        //         System.out.println("You are going to join a job");
        //         break;
        //     case 60 :
        //         System.out.println("You are going to retired");
        //         break;
        //     default:
        //         System.out.println("Enjoy Your Life");
        // }
        // //Enhanced Switch 
        // switch(age){

        //     case 18 ->System.out.println("You are going to become an Adult");
               
        //     case 23 -> System.out.println("You are going to join a job");
        //     case 60 ->System.out.println("You are going to retired");
              
        //     default->System.out.println("Enjoy Your Life");
        // }

        String website;
        System.out.print("Enter the name of the website : ");
        Scanner sc = new Scanner(System.in);
        website = sc.nextLine();
        sc.close();
        int index = website.indexOf('.');

        if (website.substring(index+1).equals("com")){
            System.out.println("It is a .com Website");
        }
        else if (website.substring(index+1).equals("org")){
            System.out.println("It is a .org Website");
        }
        else if (website.substring(index+1).equals("in")){
            System.out.println("It is a .in Website");
        }
        else {
            System.out.println("What the F is This ??");
        }
    ////////    It can be also done by .endsWith(".com")
    }

}