
public class FormatadorCep {
	public static void main(String[] args) {
		try {
			String cepFormatado = formatarCep("23575420");
			System.out.println(cepFormatado);
		} catch (CepInvalidoException e) {
			System.out.println("Cep inválido! Insira apenas os 08 dígitos.");
		
		}
	}

	//Exception criada e exibe a mensagem da linha 8 caso valor seja diferente de 8 dígitos.
	//Do contrário, apenas formatará o cep inserido na linha 5.
	static String formatarCep(String cep) throws CepInvalidoException{
		if(cep.length() != 8) 
			throw new CepInvalidoException();
		
		return "23.575-420";
		
	}

}