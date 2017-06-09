#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Evandro Padilha Barroso Filho     1715310009
# Gabriel Barroso da Silva Lima     1715310011
# Frederico Victor Alfaia Rodrigues 1515200030
# Felipe Eduardo Silva de Almeida   1715310031
# Felipe Guerreiro De Mello         1315120052
# Silas castro de Mendonça          1715310066
# 43.O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
# Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral
# do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.

carda = [0, 0, 0, 0, 0, 0]
price = [1.2, 1.3, 1.5, 1.2, 1.3, 1]
c = 1

print("faça o seu pedido: ")

while c != 0:

    code = int(input())
    quant = int(input("quantidade desejada: "))

    if (code != 100) and (code != 101) and (code != 102) and (code != 103) and (code != 104) and (code != 105):
        c = int(input("código inválido, mais algo? (1 - sim | 0 - não) "))

    else:
        code -= 100
        carda[code] += quant
        c = int(input("mais algo? (1 - sim | 0 - não) "))

code = 100
total = 0

while c < 6:

    if carda[c] != 0:
        print ("pedido de código", code, ", preço unitário: R$", price[c], ",quantidade:", carda[c], "total do item: R$", carda[c] * price[c])
        total += price[c] * carda[c]

    c += 1

print("preço total do pedido: R$", total)
