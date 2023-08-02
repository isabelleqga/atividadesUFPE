import java.util.Scanner;

public class Main {
    public static String maior(int n1, int n2) {
        if (n1 > n2){
            return "O maior é: "+n1;
        } else if (n2 > n1) {
            return "O maior é: "+n2;
        }else{
            return "Os números são iguais.";
        }
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Insira o primeiro número: ");
        int n1 = sc.nextInt();
        while (n1<=0){
            System.out.print("Insira o primeiro número: ");
            n1 = sc.nextInt();
        }
        System.out.print("Insira o segundo número: ");
        int n2 = sc.nextInt();
        while (n2<=0){
            System.out.print("Insira o segundo número: ");
            n2 = sc.nextInt();
        }
        System.out.println(maior(n1,n2));

    }
}