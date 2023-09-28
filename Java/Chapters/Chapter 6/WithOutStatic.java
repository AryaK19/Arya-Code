public class WithOutStatic {

    int add(int a ,int b){
        return a+b;
    }
    public static void main(String[] args) {
        int a = 9,b = 20;
        // add(a,b);   Cant call it as its not static and no object is created to call the function so

        WithOutStatic obj = new WithOutStatic(); //this is the way to initialise the class obj not ---->  CLASS obj;
        System.out.println(obj.add(a,b));
    }
}
