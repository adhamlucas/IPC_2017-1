#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Antonio Diego Furtado da Silva            1715310004
# João Victor de Cordeiro                   1515140036
# Matheus de Oliveira Marques               1515310514
# Reinaldo da Silva Varas                   1715310054
# Silas Castro de Mendonça                  1715310066
#
# Lista01 Questão: 5)Faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem
# e custo, que é o custo de um item antes do imposto.
# A função “altera” o valor de custo para incluir o imposto sobre vendas.
#----------------------------------------------------------------------------------------------------------------------

custo = float(input('Informe o custo do produto: '))
taxaImposto = float(input('Informe o valor da taxa de imposto: '))

def somaImposto(taxaImposto, custo):
    custo = custo + (custo * taxaImposto / 100.0)
    return custo

print("Preço sem Impostos: %.2f" %custo)

custo = somaImposto(taxaImposto, custo)

print("O preço com impostos é: %.2f" %custo)
