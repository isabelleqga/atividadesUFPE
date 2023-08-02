import java.util.Scanner;

public class Main {
    public static String parImpar(int n) {
        if (n % 2 == 0){
           return n+" é par.";
        }else{
            return n+" é ímpar.";
        }
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Insira um número: ");
        int n = sc.nextInt();
        System.out.println(parImpar(n));

    }
}