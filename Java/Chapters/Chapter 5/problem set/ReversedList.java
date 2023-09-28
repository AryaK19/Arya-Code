

public class reversedList {
    public static void main(String[] args) {
        int [] list = {1,2,3,4,5,6,7};
        int [] reversedL = new int[list.length];
        for (int i=0;i<list.length;i++){
            reversedL[list.length-i-1] = list[i] ;
        }
        for(int e : reversedL){
            System.out.printf("%d ",e);
        }
    }

}
