def converter_horas(horas):

    if horas > 12:
        nova_hora = horas - 12
        return nova_hora, 'P'

    else:
        return horas, 'A'

def imprimir_horas(horas,minutos, situacao):
    horário = ('%d:%d %s' % (horas, minutos, situacao))
    return horário

cond = True
while cond:
    print("""Conversor de horas
Digite uma hora negativa para parar o programa
    """)

    horas = int(input('Digite as horas: '))


    if horas < 0:
        cond = False

    else:

        minutos = int(input('Digite os minutos: '))

        horas = converter_horas(horas)

        horário = imprimir_horas(horas[0], minutos, horas[1])

        print(horário)
