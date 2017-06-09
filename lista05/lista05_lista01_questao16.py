# ----------------------------------------------------------
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
# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,
# 13,21,34,55,...Faça um programa que gere a série até que o
# valor seja maior que 500.
#-----------------------------------------------------------
current_fib = 0
next_fib = 1
while current_fib <= 500:
    new_fib = current_fib + next_fib
    current_fib = next_fib
    next_fib = new_fib
