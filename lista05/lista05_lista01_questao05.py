##----------------------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Kethelen Tamara Braga Barbosa           1525212002
# Lucas Gabriel Silveira Duarte           1715310053
# Luis Gustavo Moura de Queiroz           1715310037
# Luiz Daniel Raposo Nunes de Mello       1715310049
# Luiz Paulo Machado e Souza              1515200542
# 
#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
#Valide a entrada e permita repetir a operação.
#--------------------------------------------------------------------------------------------------

pop_a = float(input("Digite a população do primeiro país: "))
pop_b= float(input("Digite a população do segundo país: "))

while ( pop_a <= 0 ) or ( pop_b <= pop_a ):
    print('Valor(res) inválido(s)')
    pop_a = float(input("Digite a população do primeiro país: "))
    pop_b = float(input("Digite a população do segundo país: "))


tax_a = float(input("Digite a taxa de crescimento do primeiro país: "))
tax_b = float(input("Digite a taxa de crescimento do segundo país: "))

while tax_a <= tax_b:
    print('Taxa de crescimento do primeiro país inválida!')
    print('A Taxa de crescimento do primeiro país deve ser MAIOR que a do segundo país')
    tax_a = float(input("Digite a taxa de crescimento do primeiro país: "))
    tax_b = float(input("Digite a taxa de crescimento do segundo país: "))


years = 0

while (pop_a <= pop_b):
    pop_a = pop_a + (pop_a * tax_a)
    pop_b = pop_b + (pop_b * tax_b)
    years = years + 1

print("será necessário %i anos para o país A ultrapasar o país B" %years)
