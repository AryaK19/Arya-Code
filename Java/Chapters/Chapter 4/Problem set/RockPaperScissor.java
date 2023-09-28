import java.util.Scanner;
import java.util.Random;

public class RockPaperScissor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rn  = new Random();
        String move;
        int ran;
        int score = 0,i=1;

        while (i<=5){
            System.out.print("Enter Move (r/p/s) : ");
            move = sc.nextLine();
            ran = rn.nextInt(3);

            if (ran == 0){
                switch (move){
                    case "r":
                        System.out.println("Opponant : r");
                        System.out.println("It a Tie");
                        System.out.printf("Score : %d\n",score);
                        i+=1;
                        break;
                    case "p":
                        System.out.println("Opponant : r");
                        System.out.println("You Win :)");
                        score+=1;
                        System.out.printf("Score : %d\n",score);
                        i+=1;
                        break;
                        case "s":
                        System.out.println("Opponant : r");
                        System.out.println("You Lose :(");
                        score-=1;
                        System.out.printf("Score : %d\n",score);
                        i+=1;
                        break;

                    default:
                        System.out.println("Not Valid Input Try Again .....");

                }
            }
            else if (ran == 1){
                switch (move){
                    case "r":
                        System.out.println("Opponant : p");
                        System.out.println("You Lose :(");
                        score-=1;
                        System.out.printf("Score : %d\n",score);
                        i+=1;
                        break;
                    case "p":
                        System.out.println("Opponant : p");
                        System.out.println("Its a Tie");
                        System.out.printf("Score : %d\n",score);
                        i+=1;
                        break;
                        case "s":
                        System.out.println("Opponant : p");
                        System.out.println("You Win :)");
                        System.out.println("You Lose :(");
                        score+=1;
                        System.out.printf("Score : %d\n",score);
                        i+=1;
                        break;

                    default:
                        System.out.println("Not Valid Input Try Again .....");

                }
            }
            else{
                switch (move){
                    case "r":
                        System.out.println("Opponant : s");
                        System.out.println("You Win :)");
                        score+=1;
                        System.out.printf("Score : %d\n",score);
                        i+=1;
                        break;
                        case "p":
                        System.out.println("Opponant : s");
                        System.out.println("You Lose :(");
                        score-=1;
                        System.out.printf("Score : %d\n",score);
                        i+=1;
                        break;
                        case "s":
                        System.out.println("Opponant : s");
                        System.out.println("It a Tie");
                        System.out.printf("Score : %d\n",score);
                        i+=1;
                        break;
                        
                    default:
                        System.out.println("Not Valid Input Try Again .....");
                        
                    }
            
            }
            
        }

        sc.close();
    }
}
