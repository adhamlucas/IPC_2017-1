#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#
# Diogo Roberto Duarte da Costa     1715310056
# Felipe Eduardo Silva de Almeida   1715310031
# Felipe Guerreiro de Mello         1315120052
# Frederico Victor Alfaia Rodrigues 1515200030
# Gabriel Barroso da Silva Lima     1715310011
#
# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram
# para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, 
# baseado no salário atual:
#    salários até R$ 280,00 (incluindo) : aumento de 20%
#    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#    o salário antes do reajuste;
#    o percentual de aumento aplicado;
#    o valor do aumento;
#    o novo salário, após o aumento.
#-------------------------------------------------------------------------------------

salaryInitial = float(input("digite um salário"))

if salaryInitial <= 280:
    salaryFinal = salaryInitial * 1.2
    percentage = 20
else:
    
    if salaryInitial <= 700:
        salaryFinal = salaryIniital * 1.15
        percentage = 15
    else:
        
        if salaryInitial < 1500:
            salaryFinal = salaryInitial * 1.1
            percentage = 10
        else:
            salaryFinal = salaryInitial * 1.05
            percentage = 5
            
difference = salaryFinal - salaryInitial
print("Salário anterior: R$", salaryInitial, " reais || Salário atual: R$", salaryFinal, " reais.")
print("Percentual de aumento aplicado: ", percentage, "% || Valor do aumento: R$", difference, " reais")
