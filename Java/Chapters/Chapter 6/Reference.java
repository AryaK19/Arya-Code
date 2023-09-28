public class Reference {
    static void change(int a){
        a = 98;
    }
    static void change2(int [] arr){
        arr[0] = 98;
    }
    
    public static void main(String[] args) {
        // int x =45;
        // change(x);
        // System.out.println("The Value of x after running change is : "+x);

        // chnaging the array
        int [] marks = {52,73,77,89,98,94};
        change2(marks);
        System.out.println(marks[0]);
        // when array is passed to the method ,to reduce memory , the address (the original obj i passed) is passed it self
    }
}
