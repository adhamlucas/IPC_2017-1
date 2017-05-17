# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Gabriel barroso da Silva Lima      1715310011
# Frederico Victor Alfaia Rodrigues  1515200030
# André Luis Laborda neves           1515070006
# Diego Reis Figueira                1515070169
# Diogo Duarte
#
# Deseja-se fazer a emissão da folha de pagamento
# de uma empresa. Para cada um dos n funcionários
# da empresa são dadas as seguintes informações:
#
# NOME 
# SAL (salário) 
# HED (horas extras diurnas) 
# HEN (horas extras noturnas) 
# ND (número de dependentes) 
# FAL (faltas em horas) 
# DE (descontos eventuais) 
# REF (gastos com refeições feitas na empresa) 
# VAL (vales retirados durante o mês).
# 
# Emitir as seguintes informações:
#     
# nome, 
# salário, 
# horas extras = HED * SAL/160 + HEN * 1.2 * SAL/160, 
# salário família = ND * 0.05 * salário mínimo vigente, 
# salário bruto = salário + horas extras + salário família.
# 
# Descontos efetuados:
#    
# INAMPS = 0.08 * SAL, 
# faltas = FAL * SAL/160, 
# refeições, 
# vales, 
# descontos eventuais, 
# imposto de renda = 0.08 * salário bruto.
# 
# Salário líquido = salário bruto - desconto total. 

matriz = []
n = int(input())

for i in range (n):
    
    matriz.append([0]*9)
    
    matriz[i][0] = input("nome: ")
    matriz[i][1] = int(input("salário: "))
    matriz[i][2] = int(input("horas extras diurnas: "))
    matriz[i][3] = int(input("horas extras noturnas: "))
    matriz[i][4] = int(input("número de dependentes: "))
    matriz[i][5] = int(input("faltas em horas: "))
    matriz[i][6] = int(input("descontos eventuais: "))
    matriz[i][7] = int(input("gastos com refeições feitas na empresa: "))
    matriz[i][8] = int(input("vales retirados durante o mês: "))

print(".")

for i in range (n):
    
    exhoras = (matriz[i][2] * matriz[i][1]) / 160  + (matriz[i][3] * 1.2 * matriz[i][1]) / 160
    salfami = matriz[i][4] * 937 * 0.05
    salbruto = matriz[i][1] + exhoras + salfami
    inamps = 0.08 * matriz[i][1] 
    faltas = (matriz[i][5] * matriz[i][1])/160
    impren = salbruto * 0.08
    destot = faltas + inamps + impren + matriz[i][6] + matriz[i][7] + matriz[i][8]
    salliq = salbruto - destot
    
    print("--//--//--//--//--//--//--//--//--//--//--//--")
    print("funcionário", n)
    print("salário:", matriz[i][1])
    print("horas extras:", exhoras)
    print("salário família:", salfami)
    print("salário bruto:", salbruto)
    print("...........................")
    print("Descontos efetuados")
    print("INAMPS:", inamps)
    print("faltas:", faltas)
    print("imposto de renda:", impren)
    print("descontos totais:", destot)
    print("...........................")
    print("salário líquido:", salliq)
    print("--//--//--//--//--//--//--//--//--//--//--//--")
