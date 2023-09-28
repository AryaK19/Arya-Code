import java.util.Scanner;

class Book {
    String name;
    int location;

    Book(String name, int location) {
        this.name = name;
        this.location = location;
    }
}

class Library {

    Book[] books = new Book[100];
    Scanner sc = new Scanner(System.in);

    Library() {
        books[0] = new Book("Rich Dad Poor Dad", 100);
        books[1] = new Book("To Kill A Mocking Bird", 101);
        books[2] = new Book("The Alchemist", 102);
        books[3] = new Book("Invisible Man", 103);
        books[4] = new Book("Start With Why", 104);
    }

    public String takeInput() {
        System.out.print("\nEnter Command (show/add/remove/issue/return/exit) : ");
        String n = sc.nextLine();
        return n;
    }

    public boolean takeAction(String s) {
        switch (s) {
            case "show":
                this.showBook();
                return false;
            case "add":
                this.addBook();
                return false;
            case "remove":
                this.removeBook();
                return false;
            case "issue":
                this.issueBook();
                return false;
            case "return":
                this.returnBook();
                return false;
            default:
                return true;
        }
    }

    public void showBook() {
        System.out.println("");
        for (Book b : this.books) {
            if (b != null && b.location == 0) {
                System.out.format("Name : %s\tLocation : Not available now\n", b.name);
            } else if (b != null) {
                System.out.format("Name : %s\tLocation : %d\n", b.name, b.location);
            }
        }
        System.out.println("");
    }

    public void addBook() {
        System.out.print("Enter the Name of the Book to be added : ");
        String n = sc.nextLine();
        for (int i = 0; i < 100; i++) {
            if (this.books[i] == null) {
                this.books[i] = new Book(n, 100 + i);
                System.out.println("Book Added");
                break;
            }
        }
    }

    public void removeBook() {
        System.out.print("Enter the Name of the Book to be removed : ");
        String n = sc.nextLine();
        boolean exits = false;
        for (int i = 0; i < 100; i++) {
            if (this.books[i] != null && (this.books[i].name).equals(n)) {
                this.books[i] = null;
                System.out.println("Book Removed");
                exits = true;
                break;
            }
        }
        if (!exits) {
            System.out.println("No Such Book Found");
        }
    }

    public void issueBook() {
        System.out.print("Enter the Name of the Book to be issued : ");
        String n = sc.nextLine();
        boolean exits = false;
        for (int i = 0; i < 100; i++) {
            if (this.books[i] != null && (this.books[i].name).equals(n)) {
                this.books[i].location = 0;
                System.out.println("Book Issued");
                exits = true;
                break;
            }
        }
        if (!exits) {
            System.out.println("No Such Book Found");
        }
    }
    
    public void returnBook() {
        System.out.print("Enter the Name of the Book to be returned : ");
        String n = sc.nextLine();
        boolean exits = false;
        for (int i = 0; i < 100; i++) {
            if (this.books[i] != null && (this.books[i].name).equals(n) && this.books[i].location == 0) {
                this.books[i].location = 100 + i;
                System.out.println("Book Returned");
                exits = true;
                break;
            }
            else if (this.books[i] != null && (this.books[i].name).equals(n) && this.books[i].location != 0) {
                System.out.println("Book Not Taken");
                exits = true;
                break;
            }
        }
        if (!exits) {
            System.out.println("No Such Book Found");
        }
    }
}

public class TRY {
    public static void main(String[] args) {
        Library L = new Library();
        boolean done = false;
        String n;

        while (!done) {
            n = L.takeInput();
            done = L.takeAction(n);
        }
    }
}