numero = int(input("Digite um número menor que 1000: "))
if numero < 1000:
	centena = numero//100
	dezena = (numero%100)//10
	unidade = (numero%100)%10
	print(dezena)
else:
	print("Número inválido")
