import java.util.Locale;
import java.util.Scanner;

public class AboutMe {
	public static void main(String[] args) {
		
		try {
		Scanner scanner = new Scanner (System.in).useLocale(Locale.US);
		
		System.out.println("Digite seu nome: ");
		String nome = scanner.next();
		
		System.out.println("Digite seu sobrenome: ");
		String sobrenome = scanner.next();
		
		System.out.println("Digite sua idade: ");
		int idade = scanner.nextInt();
		
		System.out.println("Digite sua altura em cm: ");
		int altura = scanner.nextInt();
		
		System.out.println("Olá, " +nome.toUpperCase() + " " + sobrenome.toUpperCase()+ "!!");
		System.out.println("Você tem " + idade + " anos de idade!");
		System.out.println("Sua altura é " + altura + " cm");
		
		scanner.close();
		}
		
		catch (java.util.InputMismatchException e){
			System.out.println("\nOs campos Idade e Altura devem ser numéricos!");
		}
	}
}
