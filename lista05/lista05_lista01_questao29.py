# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Kethelen Tamara Braga Barbosa           1525212002
# Lucas Gabriel Silveira Duarte           1715310053
# Luis Gustavo Moura de Queiroz           1715310037
# Luiz Daniel Raposo Nunes de Mello       1715310049
# Luiz Paulo Machado e Souza              1515200542
# 

#---------------------------------------------------------------------------------------------------------------------
#O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente
#deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a 
#atendente o caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver
#o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:
#Lojas Quase Dois - Tabela de preços
#1 - R$ 1.99
#2 - R$ 3.98
#...
#50 - R$ 99.50



cont = 1
while cont <= 50:
    print (cont,"-R$", cont * 1.99)
    cont = cont + 1


