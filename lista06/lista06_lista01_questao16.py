#----------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Alexandre Marques Uchôa           1715310028
# Carlos Eduardo T. de Oliveira     1715310030
# Hugo Thadeu Silva Cardoso         1715310013
# Judá Salazar Braga                1515200050
# Kethelen Tamara Braba Barbosa     1525212002


#---------------------------------------------------------------------------
l=[]
inicio=int(input("De qual valor: "))
lim=int(input("Até qual valor: "))
com=0
for com in range(100000000000):
    sal=200+(9*com)/100
    m= ["vendedor %d" %com , sal]
    l.append(m)
    if sal > lim:
        break
    if sal >= inicio:
        print(l[com])
print("Número de Vendedores (ou como quiser chamar) %d" %com)
print("Maior Salário do Povo: %d" %sal)
