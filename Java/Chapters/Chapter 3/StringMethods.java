

public class StringMethods{
    public static void main(String[] args){
        String name = "Arya";
        System.out.println(name);
        int value = name.length();
        System.out.println(value);
        String lower = name.toLowerCase();
        System.out.println(lower);
        String upper = name.toUpperCase();
        System.out.println(upper);

        String nonTrimString = "  ARYA  Kadam   ";
        System.out.println(nonTrimString);
        String trimedString = nonTrimString.trim() ;
        System.out.println(trimedString);

        System.out.println(name.substring(2));

        System.out.println(name.replace('A', 'a'));
        
        System.out.println(name.replace("Arya", "aryak"));
        System.out.println(name);

        System.out.println(name.startsWith("Ar"));
        System.out.println(true&false);
        
        String modifiedName = "AryaaArya";
        System.out.println(name.charAt(2));
        System.out.println(modifiedName.indexOf('a'));
        System.out.println(modifiedName.indexOf("ry",3));
        
        System.out.println(modifiedName.lastIndexOf("ry"));
        System.out.println(name.equals("Arya"));
        System.out.println(name.equalsIgnoreCase("AryA"));

        System.out.println("\" , \t , \' , \n , Arya");


        
    }
}