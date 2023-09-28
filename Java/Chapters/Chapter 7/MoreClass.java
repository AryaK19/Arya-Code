
class Employee{
    int id;
    String name;
    public void printDetails(){
        System.out.println("DETAIL NY METHODS : ");
        System.out.println(id);
        System.out.println(name);
    }
}

public class MoreClass {
    public static void main(String[] args) {
        Employee arya = new Employee();
        arya.id= 29;
        arya.name = "ARYA KADAM";

        System.out.println(arya.id);
        System.out.println(arya.name);

        arya.printDetails();
    }
}
