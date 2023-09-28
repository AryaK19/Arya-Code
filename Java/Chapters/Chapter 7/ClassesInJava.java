
public class ClassesInJava {
    static public class Shape{ // same thing happens like methods , we have to use static
        int a=100;
        int b = 1;
        public void sum(){
            System.out.println(a+b);
        }

    }
    public static void main(String[] args) {
        Shape obj = new Shape();
        obj.sum();
    }
}
