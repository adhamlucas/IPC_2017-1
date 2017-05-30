#-----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey                 1715310059
# Evandro Padilha Barroso Filho         1715310009
# Felipe Eduardo Silva de Almeida       1715310031
# Joelson Pereira Lima			1715310060
# Víctor Hugo de Oliveira Carreira      1715310063
#
#Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12.
#Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é
#chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é
#continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto
#novamente. 
#-----------------------------------------------------------------------------------------------------------------------

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
