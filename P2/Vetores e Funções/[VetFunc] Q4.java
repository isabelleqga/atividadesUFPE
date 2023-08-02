import java.util.Scanner;

public class Main {
    public static void dividir100(float [] numeros) {
        System.out.println("Conteúdo dividido por 100: ");
        for (int i = 0; i < 5; i++) {
            numeros[i] = numeros[i]/100;
            System.out.println(numeros[i]);
        }
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        float[] numeros =  new float[5];

        for (int i = 0; i < 5; i++) {
            System.out.print("Insira o dado da posição "+(i+1)+": ");
            numeros[i] = sc.nextFloat();
        }

        dividir100(numeros);

    }
}