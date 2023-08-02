import java.util.Scanner;

public class Main {
    public static String fazerBusca(float [] numeros, int chave) {
        for (int i = 0; i < 5; i++) {
            if (numeros[i] == chave){
                return "Chave encontrada na posição: "+(i+1);
            }
        }
        return "Chave não encontrada!";
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        float[] numeros =  new float[5];

        for (int i = 0; i < 5; i++) {
            System.out.print("Insira o dado da posição "+(i+1)+": ");
            numeros[i] = sc.nextFloat();
        }

        System.out.print("Insira a chave de busca: ");
        int chave = sc.nextInt();

        System.out.println(fazerBusca(numeros, chave));

    }
}