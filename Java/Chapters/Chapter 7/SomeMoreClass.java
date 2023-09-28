class Employee{
    int id;
    String name;
    int salary;
    public void setId(int i){
        id = i;
    }
    public void setName(String n){
        name = n;
    }
    public void setSalary(int s){
        salary = s;
    }


    public int getId(){
        return id;
    }
    public String getName(){
        return name;
    }
    public int getSalary(){
        return salary;
    }
}

public class SomeMoreClass {
    public static void main(String[] args) {
        Employee arya = new Employee();

        // arya.setId(29);
        arya.setSalary(120000);
        // arya.setName("ARYA");
        
        System.out.println(arya.getId());
        System.out.println(arya.getSalary());
        System.out.println(arya.getName());
    }
}
