#----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Gabriel de Queiroz Sousa                  1715310044
# Lucas Gabriel Silveira Duarte             1715310053
#
#  Faça uma função que recebe, por parâmetro, a altura (alt) e o 
#sexo de uma pessoa e retorna o seu peso ideal. 
#Para homens, calcular o peso ideal usando 
#a fórmula peso ideal = 72.7 x alt - 58 e, 
#para mulheres, peso ideal = 62.1 x alt - 44.7.  
#----------------------------------------------------------------------------------------------------------------------

altura = float(input("digite a sua altura em metros: "))

sexo = input("Informe seu sexo(m para masculino, f para feminino): ")

def peso_ideal(altura):
    if sexo == "m":
        altura = 72.7 * altura - 58
    if sexo == "f":
        altura = 62.1 * altura - 44.7
    return altura

print("O seu peso ideal é:",peso_ideal(altura))
