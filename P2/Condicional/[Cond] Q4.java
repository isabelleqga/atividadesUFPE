import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.print("Insira o primeiro valor: ");
        int n1 = sc.nextInt();
        System.out.print("Insira o segundo valor: ");
        int n2 = sc.nextInt();

        if (n1 == n2){
            System.out.println("Multiplicação: "+(n1*n2));
        }else if (n1>n2){
            System.out.println("Subtração: "+(n1-n2));
        }else{
            System.out.println("Soma: "+(n1+n2));
        }

    }
}