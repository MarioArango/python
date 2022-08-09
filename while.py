def potencias(base, limite):
    exponente = 0
    potencia = base**exponente
    while potencia < limite:
        print(potencia)
        exponente = exponente + 1
        potencia = base**exponente


if __name__ == '__main__':
    base = int(input('Ingrese la base: '))
    limite = int(input('Ingrese el limite: '))
    potencias(base, limite)