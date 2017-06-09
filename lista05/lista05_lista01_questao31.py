# --------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# ULISSES ANTONIO ANTONINO DA COSTA - 1515090555
# TIAGO FERREIRA ARANHA - 1715310047
# VÍTOR SIMÕES AZEVEDO - 1715310025
# VICTOR HUGO DE OLIVEIRA CARREIRA - 1715310063
# REINALDO VARGAS - 1715310054
#
# O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
# Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
# Um valor zero deve ser informado pelo operador para indicar o final da compra.
# O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco.
# Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:
# Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
#
# --------------------------------------------------------------------------
# primeiro while para controlar o registro das compras
while True:
    print('Loja Tabajara')
    cont = 1
    total = 0
    # segundo while para calcular cada produto
    while True:
        valor = float(input("Produto {}: R$ ".format(cont)))
        cont += 1
        total += valor
        # se for digitado 0 encerra a compra
        if valor == 0:
            break
    # calculo do Total e troco
    print('Total: ', total)
    din = float(input('Dinheiro :'))
    # Condição do dinheiro for menor que o total
    if din >= total:
        troco = din - total
        print('Troco: ', troco)
    else:
        print('Dinheiro insuficiente')
        din = float(input('Dinheiro :'))
        troco = din - total
        print('Troco: ', troco)

    reset = input('Pressione 0 para reiniciar ou 1 para encerrar: ')
    if reset == '0':
        continue
    else:
        print('Finalizando compra')
        break
