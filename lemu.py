numero = int(input("Digite um número menor que 1000: "))
if numero < 1000:
	centena = numero//100
	dezena = (numero%100)//10
	unidade = (numero%100)%10
	print("O número tem",centena,"cetenas,",dezena,"dezenas e",unidade,"unidades.")
else:
	print("Número inválido")
