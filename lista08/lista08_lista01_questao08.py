number = int(input("digite um número para saber quantos dígitos ele possui: "))

def qnt_digitos(number):
    number = str(number)
    number = len(number)
    return number

print("o número digitado possui:",qnt_digitos(number),"digitos")
