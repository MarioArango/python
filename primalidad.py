def primalidad(numero):
    validator = True
    for item in range(1, numero + 1):
        if item == 1 or item == numero:
            continue
        elif numero%item == 0 :
            validator = False
    if validator:
        print('Es primo')
    else:
        print('No es primo')

if __name__ == "__main__":
    numero = int(input('Ingresa un número: '))
    primalidad(numero)
