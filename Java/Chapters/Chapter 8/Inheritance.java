
class Base{
    int x = 9;
    int y = 10;

    public void getX(){
        System.out.println("The Value of x : "+x);
    }
    public void getY(){
        System.out.println("The Value of y : "+y);
    }
}

class Derived extends Base{
    int v= 0;
    public void getV(){
        System.out.println("The Value of v : "+v);
    }
}

public class Inheritance {
    public static void main(String[] args) {
        Base b = new Base();
        b.getX();
        Derived d = new Derived();
        d.getX();
    }
}
