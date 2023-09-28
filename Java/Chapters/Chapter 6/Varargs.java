public class Varargs{
    // static int sum(int a,int b){
    //     return a+b;
    // }
    // static int sum(int a,int b,int c){
    //     return a+b+c;
    // }
    // static int sum(int a,int b,int c,int d){
    //     return a+b+c+d;
    // }


    static int sum(int ...arr){
        // it is available as int [] arr
        int result = 0;
        for(int a:arr){
            result +=a;
        }
        return result;
    }
    public static void main(String[] args) {
        System.out.println("Wellcome to Varargs tut");
        System.out.println("The of sum of 4 and 5 is: "+sum(4,5));
        System.out.println("The of sum of 4 and 5 is: "+sum(4,5,6));
        System.out.println("The of sum of 4 and 5 is: "+sum(4,5,6,12,324));
        System.out.println("The of sum of 4 and 5 is: "+sum(4,5,6,12,324,213,12,312,12,312,312,3123,123));


        // Hence to impliment multiple arguments without use of function overloading we use varargs

        // can pass no valuse as well (as an empty array)

    }
}