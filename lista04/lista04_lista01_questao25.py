#--------------------------------------------------------------------------
#Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
#=======================================================================================
#Reinaldo da Silva Vargas 1715310054
#Natalia Cavalcante Xavier 1715310021
#Nayara da Silva Cerdeira da Costa 1715310038
#Marcus Vinicius Paes da Silva Santos 1515070060
#Matheus de Oliveira Marques 1515310514
#========================================================================================
#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a #participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser #classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, #ele será classificado como "Inocente".

print("DIGITE 1 PARA(SIM) OU DIGITE (0) PARA NAO")

phone1 = int(input("TELEFONOU PARA A VITIMA?"))
phone2 = int(input("ESTEVE NO LOCAL DO CRIME?"))
phone3 = int(input("MORA PERTO DA VITINMA?"))
phone4 = int(input("DEVIA PARA A VITIMA?"))
phone5 = int(input("JA TRABALHOU PARA A VITIMA?"))

result = (phone1+ phone2+phone3+phone4+phone5)

if result == 2 :
    print("suspeito")
elif result > 2 and result <= 4:
    print("cumplice")
elif result >= 5:
    print("culpado")
else:
    print("ta de boa")
