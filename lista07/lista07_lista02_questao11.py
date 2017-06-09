#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Erik Atilio Silva Rey                 1715310059
# Evandro Padilha Barroso Filho         1715310009
# Felipe Eduardo Silva de Almeida       1715310031
# Joelson Pereira Lima 			        1715310060
# Víctor Hugo de Oliveira Carreira      1715310063
#
#11.(FEA 85) Deseja-se atualizar as contas correntes dos clientes de uma agência bancária. É dado o cadastro de n clie
#ntes contendo para cada cliente o número de sua conta e o seu saldo; o cadastro está ordenado pelo número da conta. Em
#seguida, é dado o número de operações efetuadas no dia e, para cada operação, o número da conta, uma letra C ou D
#indicando se a operação é de crédito ou débito e o valor da operação . Emitir o cadastro de clientes atualizado.
#
#-----------------------------------------------------------------------------------------------------------------------
linhas = int(input())
matriz_clientes = []
colunas = 2

for i in range(linhas):
    linha = []
    for i in range(colunas):
        linha.append(int(input()))
    matriz_clientes.append(linha)

operacoes_efetuadas = int(input())
numero_cadastro = int(input("numero de cadastro: "))

for x in range(operacoes_efetuadas):
    operacao = input('c ou d: ')
    quantia = int(input("quantia:"))
    if operacao == 'c':
        matriz_clientes[numero_cadastro-1][1] +=  quantia
    if operacao == 'd':
        matriz_clientes[numero_cadastro-1][1] -= quantia
    quantia = 0

print(matriz_clientes)








