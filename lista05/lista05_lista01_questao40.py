# -----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Grupo 08
# Victor Summer Oliveira Pantaleao 1715310042
# Walter Nobre Da Silva Conceição  1715310057
# Wesley da Silva Rocha            1715310026
# Wilbert Luís Evangelista Marins  1715310055
# Yuri Leandro de Aquino Silva     1615100462
#
# Foi feita uma estatística em cinco cidades brasileiras para
# coletar dados sobre acidentes de trânsito. Foram obtidos os
# seguintes dados:
#   A. Código da cidade;
#   B. Número de veículos de passeio (em 1999);
#   C. Número de acidentes de trânsito com vítimas (em 1999).
#      Deseja-se saber:
#   D. Qual o maior e menor índice de acidentes de transito e
#      a que cidade pertence;
#   E. Qual a média de veículos nas cinco cidades juntas;
#   F. Qual a média de acidentes de trânsito nas cidades com
#      menos de 2.000 veículos de passeio.
# -----------------------------------------------------------

# Variáveis para cálculo do menor e maior índice de
# acidentes de trânsito
menor_quantidade_de_acidentes = 2**63 
codigo_da_cidade_com_menor_quantidade_de_acidentes = None
maior_quantidade_de_acidentes = -1
codigo_da_cidade_com_maior_quantidade_de_acidentes = None

# Variável para cálculo da quantidade média de veículos
quantidade_media_de_veiculos = 0

# Variáveis para cálculo da quantidade média de acidentes
# de trânsito em cidades com menos de 2000 veículos
quantidade_media_de_acidentes = 0
quantidade_de_cidades_com_menos_de_dois_mil_veiculos = 0

quantidade_de_cidades = 0
while quantidade_de_cidades < 5:
    codigo_da_cidade = input()
    quantidade_de_veiculos = int(input())
    quantidade_de_acidentes = int(input())

    # Cálculo do menor índice de acidentes
    if quantidade_de_acidentes < menor_quantidade_de_acidentes:
        menor_quantidade_de_acidentes = quantidade_de_acidentes
        codigo_da_cidade_com_menor_quantidade_de_acidentes = codigo_da_cidade

    # Cálculo do maior índice de acidentes
    if quantidade_de_acidentes > maior_quantidade_de_acidentes:
        maior_quantidade_de_acidentes = quantidade_de_acidentes
        codigo_da_cidade_com_maior_quantidade_de_acidentes = codigo_da_cidade

    # Cálculo da quantidade média de veículos
    quantidade_media_de_veiculos += quantidade_de_veiculos

    # Cálculo da quantidade média de acidentes
    if quantidade_de_veiculos < 2000:
        quantidade_media_de_acidentes += quantidade_de_veiculos
        quantidade_de_cidades_com_menos_de_dois_mil_veiculos += 1

    quantidade_de_cidades += 1

print('A cidade de código {} possui o menor índice de acidentes de trânsito ({}).'.format(
    codigo_da_cidade_com_menor_quantidade_de_acidentes, menor_quantidade_de_acidentes))

print('A cidade de código {} possui o maior índice de acidentes de trânsito ({}).'.format(
    codigo_da_cidade_com_maior_quantidade_de_acidentes, maior_quantidade_de_acidentes))

quantidade_media_de_veiculos /= quantidade_de_cidades
print('Quantidade média de veículos: {}'.format(quantidade_media_de_veiculos))

if quantidade_de_cidades_com_menos_de_dois_mil_veiculos == 0:
    print('Não existe cidades com menos de dois mil veículos')
else:
    quantidade_media_de_acidentes /= quantidade_de_cidades_com_menos_de_dois_mil_veiculos
    print('Quantidade média de acidentes: {}'.format(quantidade_media_de_acidentes))
