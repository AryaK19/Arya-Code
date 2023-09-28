

public class ARRAY {
    public static void main(String[] args) {
        System.out.println("No. 1 ");
        int [] array = new int[5];
        for (int i=0;i<5;i++){
            array[i]=1;
        }
        for (int i=0;i<5;i++){
            
            System.out.println(array[i]);
        }
        
        System.out.println("No. 2 ");
        int [] marks = {1,2,3,4,5};
        
        for (int i=0;i<5;i++){
            
            System.out.println(marks[i]);
        }
        System.out.println("No. 3 ");
        
        int [] kka;
        kka = new int[5];
        for (int i=0;i<5;i++){
            kka[i]=1;
        }
        for (int i=0;i<5;i++){
            
            System.out.println(kka[i]);
        }
        
        
        
        /// godd they at least added some thing 
        
        System.out.println("No. 4 ");
        for (int element: marks){
            System.out.println(element);
        }
        
        
        
        //////////////////////////////////////////////////////
        // 2D array 
        System.out.println("2D Array ");
        
        int [][] m = {{1,2},{2,2},{3,3}};
        for (int[] e : m)
        for (int element: e){
            System.out.println (element);
        }







    }
}

