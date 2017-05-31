altura = float(input("digite a sua altura em metros: "))

sexo = input("Informe seu sexo(m para masculino, f para feminino): ")

def peso_ideal(altura):
    if sexo == "m":
        altura = 72.7 * altura - 58
    if sexo == "f":
        altura = 62.1 * altura - 44.7
    return altura

print("O seu peso ideal é:",peso_ideal(altura))