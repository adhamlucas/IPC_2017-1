#---------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Ulisses Antonio Antonino da Costa 1515090555
# Walter Nobre da Silva conceição   1715310057
# Jandinne Duarte de Oliveira       1015070265
# Vitor Summer Oliveira Pantaleão   1715310042
# Reinaldo vargas                   1715310054
#
# Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações: 
# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:
# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro

# Você foi contratado para desenvolver um programa que leia o resultado da
# enquete e informe ao final o resultado da mesma. O programa deverá ler
# os valores até ser informado o valor 0, que encerra a entrada dos dados.
# Não deverão ser aceitos valores além dos válidos para o programa (0 a 6).
# Os valores referentes a cada uma das opções devem ser armazenados num vetor.
# Após os dados terem sido completamente informados, o programa deverá calcular
# a percentual de cada um dos concorrentes e informar o vencedor da enquete.
# O formato da saída foi dado pela empresa, e é o seguinte:

# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
#------------------------------------------------------------------------------

votes = [0, 0, 0, 0, 0, 0]
so = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
totalvotes = 0
count = 0

print('Qual é o melhor SO para uso em servidores?')
print("1. %s" % so[0])
print("2. %s" % so[1])
print("3. %s" % so[2])
print("4. %s" % so[3])
print("5. %s" % so[4])
print("6. %s" % so[5])
print("0. fim da votação")


votes1 = 0
votes2 = 0
votes3 = 0
votes4 = 0
votes5 = 0
votes6 = 0


while count == 0:
    votes = int(input("Digite seu SO preferido: "))

    if votes == 0: break

    if votes == 1:
        votes1 = votes1 + 1
    elif votes == 2:
        votes2 = votes2 + 1
    elif votes == 3:
        votes3 = votes3 + 1
    elif votes == 4:
        votes4 = votes4 + 1
    elif votes == 5:
        votes5 = votes5 + 1
    elif votes == 6:
        votes6 = votes6 + 1

    totalvotes = totalvotes + 1

perc_1 = (votes1 * 100) / totalvotes
perc_2 = (votes2 * 100) / totalvotes
perc_3 = (votes3 * 100) / totalvotes
perc_4 = (votes4 * 100) / totalvotes
perc_5 = (votes5 * 100) / totalvotes
perc_6 = (votes6 * 100) / totalvotes


print("Sistema Operacional  Votos   (%) ")
print("-------------------  -----   --- ")
print(so[0],         votes1,         "%.0f" %perc_1,"%")
print(so[1],         votes2,         "%.0f" %perc_2,"%")
print(so[2],         votes3,         "%.0f" %perc_3,"%")
print(so[3],         votes4,         "%.0f" %perc_4,"%")
print(so[4],         votes5,         "%.0f" %perc_5,"%")
print(so[5],         votes6,         "%.0f" %perc_6,"%")
print("-------------------     -----")
print("Total", totalvotes)
