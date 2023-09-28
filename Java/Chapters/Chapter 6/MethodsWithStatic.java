

public class MethodsWithStatic {

    static int add(int a,int b){
        return a+b;
    }
    static void assign2(int a){
        a = 2;
    }
    public static void main(String[] args) {
        int a=6,b=7;
        System.out.println(add(a,b));
        assign2(a);
        System.out.println(a);
    }
}
