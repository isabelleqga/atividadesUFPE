import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Digite 1 para somar;\nDigite 2 para subtrair; \nDigite 3 para multiplicar; \nDigite 4 para dividir;");
        int operador = sc.nextInt();
        System.out.print("Insira o primeiro valor: ");
        int n1 = sc.nextInt();
        System.out.print("Insira o segundo valor: ");
        int n2 = sc.nextInt();

        switch (operador){
            case 1:
                System.out.println("Soma: "+ (n1+n2));
                break;
            case 2:
                System.out.println("Subtração: "+ (n1-n2));
                break;
            case 3:
                System.out.println("Multiplicação: "+ (n1*n2));
                break;
            case 4:
                if (n2 != 0){
                    System.out.println("Divisão: "+ (n1/n2));
                }else{
                    System.out.println("Divisão por zero.");
                }
                break;
        }

    }
}