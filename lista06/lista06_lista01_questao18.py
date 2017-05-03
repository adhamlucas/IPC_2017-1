#----------------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey                 1715310059
# Evandro Padilha Barroso Filho         1715310009
# Felipe Eduardo Silva de Almeida       1715310031
# Nayara da Silva Cerdeira da Costa     1715310038
# Joelson Pereira Lima 			        1715310060
# Ian Gabriel Costa Machado             1215120276
#
#18)Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador
#após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas,
#para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de
#programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da
#camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for
#digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número.
#Após o final da votação, o programa deverá exibir:
#O total de votos computados;
#Os númeos e respectivos votos de todos os jogadores que receberam votos;
#O percentual de votos de cada um destes jogadores;
#O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de
#votos dados a ele.
#----------------------------------------------------------------------------------------------------------------------------

c = 1
jogadores = []

print("qual o melhor jogador?")
while c != 0:
    voto = int(input("Digite um número entre 1 e 23 correspondente a camisa do jogador: "))
    if voto == 0:
        c = voto
    if voto > 23:
        while voto > 23:
            print("Número invalido!")
            voto = input("Digite um número entre 1 e 23 correspondente a camisa do jogador: ")
    if 0 < voto <= 23:
        jogadores.append(voto)

size = int(len(jogadores))
print("O total de votos computados =", size)

jogadores.sort()

somas = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
i = 0
while i < size:
    verificar = int(jogadores[i])
    if verificar == 1:
        somas[0] += 1
    elif verificar == 2:
        somas[1] += 1
    elif verificar == 3:
        somas[2] += 1
    elif verificar == 4:
        somas[3] += 1
    elif verificar == 5:
        somas[4] += 1
    elif verificar == 6:
        somas[5] += 1
    elif verificar == 7:
        somas[6] += 1
    elif verificar == 8:
        somas[7] += 1
    elif verificar == 9:
        somas[8] += 1
    elif verificar == 10:
        somas[9] += 1
    elif verificar == 11:
        somas[10] += 1
    elif verificar == 12:
        somas[11] += 1
    elif verificar == 13:
        somas[12] += 1
    elif verificar == 14:
        somas[13] += 1
    elif verificar == 15:
        somas[14] += 1
    elif verificar == 16:
        somas[15] += 1
    elif verificar == 17:
        somas[16] += 1
    elif verificar == 18:
        somas[17] += 1
    elif verificar == 19:
        somas[18] += 1
    elif verificar == 20:
        somas[19] += 1
    elif verificar == 21:
        somas[20] += 1
    elif verificar == 22:
        somas[21] += 1
    elif verificar == 23:
        somas[22] += 1
    i += 1
soma_verdade = []
for i in somas:
    if i != 0:
        soma_verdade.append(i)
a = 0
soma_de_votos = 0
while a < len(soma_verdade):
    soma_de_votos += int(soma_verdade[a])
    a += 1

x = 0
size2 = int(len(soma_verdade))
while x < size2:
    print("Camisa ",jogadores[x]," teve ",soma_verdade[x]," votos")
    x += 1
y = 0
percentuais = []
while y < size2:
    bom = int(soma_verdade[y])
    percentual = (bom*100)/size2
    percentuais.append(percentual)
    y += 1

w = 0
while w < size2:
    print("Percentual de votos do camisa", jogadores[w], "é = %.2f" % percentual, "%")
    w += 1

maior = 0
posicao = 0
z = 0
while z < size2:
    vencedor = int(soma_verdade[z])
    if vencedor > maior:
        maior = vencedor
        posicao = z+1
    z += 1
print("O número do jogador escolhido como o melhor jogador da partida é ",posicao," com o número de votos ",maior," e o percentual de votos dados a ele = %.2f"%percentuais[maior],"%")
