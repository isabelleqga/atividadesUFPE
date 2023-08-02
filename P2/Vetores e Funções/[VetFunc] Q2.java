import java.util.Scanner;

public class Main {
    public static String isFirstGreater(int [] numeros) {
        if (numeros[0] > numeros[1] && numeros[0] > numeros[2]){
            return "Condição satisfeita.";
        }else{
            return "Erro.";
        }
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int[] numeros = new int[3];

        System.out.print("Insira o primeiro número: ");
        numeros[0] = sc.nextInt();
        System.out.print("Insira o segundo número: ");
        numeros[1] = sc.nextInt();
        System.out.print("Insira o terceiro número: ");
        numeros[2] = sc.nextInt();

        System.out.println(isFirstGreater(numeros));

    }
}