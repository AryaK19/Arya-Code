
class Employee{

    int id;
    String name;
    int salary;

    Employee(int i , String n , int s){
        id = i;
        name = n;
        salary = s;
    }
}


public class Constructors {
    public static void main(String[] args) {
        Employee arya = new Employee(29,"ARYA", 120000000);
        System.out.println(arya.id);
        System.out.println(arya.name);
    }
}
