import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = -1;

        int cont = 0;
        while (n != 0){
            System.out.print("Insira um numero: ");
            n = sc.nextInt();
            if (n > 0){
                cont += 1;
            }
        }

        System.out.print("Quantidade de positivos: " + cont);
    }
}