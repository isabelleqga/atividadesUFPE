import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Insira um número: ");
        int n = sc.nextInt();
        boolean ehPrimo = true;

        if (n <= 1) {
            ehPrimo = false;
        }else{
            for (int i = 2; i <= Math.sqrt(n); i++) {
                if (n % i == 0) {
                    ehPrimo = false;
                }
            }
        }

        if (n > 1 && ehPrimo) {
            System.out.println(n + " é primo.");
        } else {
            System.out.println(n + " não é primo.");
        }
    }

}