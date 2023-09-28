
import java.util.Scanner;
import java.util.Random;

class Game {

    Scanner sn;
    boolean gameOver = false;
    int num;
    int playerChoice;
    int tries = 0;

    Game(Scanner s, int e) {
        Random rn = new Random();
        num = rn.nextInt(e);
        sn = s;
    }

    public boolean isOver() {
        if (num > playerChoice) {
            System.out.println("Choose a Bigger Value.....");
            gameOver = false;
        } else if (num < playerChoice) {
            System.out.println("Choose a Smaller Value.....");
            gameOver = false;
        }
        else if (playerChoice == num) {
            System.out.println("Number of Tries : " + tries);
            gameOver = true;
            
        } 
        
        return gameOver;
    }

    public void takeInput() {
        System.out.print("Enter the Guess : ");
        playerChoice = sn.nextInt();
        tries += 1;
    }

    public void checkTries() {
        
    }

}

public class GuessnigGame {
    public static void main(String[] args) {

        Scanner sn = new Scanner(System.in);
        System.out.print("Enter the Range to play with : ");
        int end = sn.nextInt();

        Game game = new Game(sn, end);
        boolean done = false;

        while (!done) {
            game.takeInput();
           
            done = game.isOver();
        }
        sn.close();
    }
}
