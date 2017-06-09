#---------------------------------------------------------------------
#Introdução a Programação dos Computadores - IPC
#Universidade do Estado do Amazonas - UEA
#Prof. Jucimar Jr.
#Dayana Picanço Marquez         1715310058
#Felipe Guerreiro de Mello      1315120052
#Faça um programa que receba uma hora (uma variável para hora e outra para minutos,
#calcule e mostre:
#a)a hora digitada convertida em minutos;
#b)a total dos minutos, ou seja, os minutos digitados mais a conversão anterios;
#c)a total dos minutos convertidos em segundos.
#---------------------------------------------------------------------

hour = int(input())
minutes = int(input())

#a)
hour_minute = hour*60

#b)
total_minute = minutes + hour_minute

#c)
total_sec = total_minute*60

print (hour_minute)
print (total_minute)
print (total_sec)
