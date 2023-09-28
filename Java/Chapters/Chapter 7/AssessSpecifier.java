
class Employee{
    private int id;
    private String name;
    int salary;
    public void setId(int i){
        this.id = i;  // We can use this. too
    }
    public void setName(String n){
        name = n;
    }
    public void setSalary(int s){
        this.salary = s;
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

public class AssessSpecifier {
    public static void main(String[] args) {
        Employee arya = new Employee();
        // arya.id = 29;  Not available as private
        // arya.setId(29);
        arya.setSalary(120000);
        // arya.setName("ARYA");
        
        System.out.println(arya.getId());
        System.out.println(arya.getSalary());
        System.out.println(arya.getName());
    }
}
