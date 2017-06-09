# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Aracille de Souza Barbosa           1315120206
# Felipe Eduardo Silva de Almeida     1715310031
# Kethelen Tamara Braga               1525212002
# Nayara da Silva Cerdeira da Costa   1715310038
# Vitor Summer Oliveira Pantaleão     1715310042
# Yuri Leandro de Aquino Silva        1615100462
#
# João Papo-de-Pescador, homem de bem, comprou um
# microcomputador para controlar o rendimento diário
# de seu trabalho. Toda vez que ele traz um peso de peixes
# maior que o estabelecido pelo regulamento de pesca do
# estado de São Paulo (50 quilos) deve pagar uma multa de
# R$ 4,00 por quilo excedente. João precisa que você faça
# um programa que leia a variável peso (peso de peixes) e
# verifique se há excesso. Se houver, gravar na variável
# excesso e na variável multa o valor da multa que João
# deverá pagar. Caso contrário mostrar tais variáveis com
# o conteúdo ZERO.
# ----------------------------------------------------------

weight = float(input("Digite o peso: ")) # criando uma variável do tipo flutuante para receber o peso digitado
limp = 50.00 # atribuindo o valor de 50.00 kg para a variável
excess = float (weight - limp) # fórmula que calcula o excesso de peso e armazena em uma variável do tipo flutuante
if weight > limp: # inicialização da condição 'se', caso esta condição seja satisfeita então será feito o que se segue abaixo
	mulct   = (excess * 4) # atribuindo o valor do produto do excesso com 4 à variavel multa
	print ("excesso foi de ", excess) # imprimindo o excesso de peso
	print ("a multa foi", mulct) # imprimindo o valor da multa pelo excesso
else: # prosseguindo com a condição 'se-senão', caso a condição acima não seja satisfeita
	print ("Excesso = ZERO") # imprimindo na tela a frase entre parênteses
	print ("Multa = ZERO") # imprimindo na tela a frase entre parênteses
