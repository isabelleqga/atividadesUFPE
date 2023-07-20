import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Insira o valor de A: ");
        int a = sc.nextInt();
        System.out.print("Insira o valor de B: ");
        int b = sc.nextInt();
				
		if (a < b) {
            for (int i = a+1; i < b; i++){
                System.out.print(i + " ");
	        }
        }else{
            for (int i = a-1; i > b; i--){
                System.out.print(i + " ");
	        }
        }

    }
}