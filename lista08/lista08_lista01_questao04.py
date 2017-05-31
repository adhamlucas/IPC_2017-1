number = int(input("digite um número: "))

def arg_porn(number):
    if number > 0 and number != 0:
        number = "P"
    else:
        number = "N"
    return number

print(arg_porn(number))