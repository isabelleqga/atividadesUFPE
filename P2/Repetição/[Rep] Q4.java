import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Insira o valor de A: ");
        int a = sc.nextInt();
        System.out.print("Insira o valor de B: ");
        int b = sc.nextInt();
				

        for (int i = a; i < b; i++){
            if (i%2 != 0){
               System.out.println("É ímpar: " + i); 
            }
	    }

    }
}