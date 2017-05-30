from ipc import vetor

inicio = input("Digite qualquer tecla para começar: ")

dados_soma = 0

dados_soma = vetor.jogar_dados()
if dados_soma == 7 or dados_soma == 11:
	print("Você ganhou! Numero =", dados_soma)
elif dados_soma == 2 or dados_soma == 3 or dados_soma == 12:
	print("Você perdeu! Numero =", dados_soma)
elif dados_soma in range(4,6) or dados_soma in range(8,10):
	print("Continue jogando, seu numero foi",dados_soma,", digite A para continuar")
	ativador = input()
	ativador = ativador.lower()
	if ativador == "a":
		dados_soma1 = 0
		dados_soma1 = vetor.jogar_dados()
		print("O numero foi", dados_soma1)
		if dados_soma1 == 7:
			print("Voce perdeu")
		elif dados_soma != 7:
			print("Voce ganhou!")
