import random

def volver_jugar(estado):
    opcion = 1
    if estado == 'gano':
        opcion = int(input('''
            ----¿Quiéres jugar otra vez?----
            1. Sí
            2. No
            ---------------***--------------
            '''))
    elif estado == 'perdio':
        opcion = int(input('''
                    *** Game Over ***
            -----Se acabaron tus intentos-----
            ¿Quiéres volver a jugar?.
            1. Sí
            2. No
            ---------------***-----------------
            '''))

    if opcion == 1:
        adivina()
    elif opcion == 2:
            print('------Fin------')


def adivina():
    limite = int(input('Ingresa el limite: '))
    numero_intentos = int(input('Ingresa el número de intentos: '))

    meta = random.randint(1, limite)
    print(meta)
    numero = int(input('Ingresa un número: '))
    intentos = 1 

    while (numero != meta) and (intentos < numero_intentos):
        if numero > meta:
            intentos += 1
            print('El numero es más pequeño')
        elif numero < meta: 
            intentos += 1
            print('El numero es mas grande')
        numero = int(input('Ingresa otro número: '))

    if numero == meta:
        print(f'''
        Lo lograste, acertaste en el {intentos} intento.
        El número fue: {numero}
        ''')
        volver_jugar('gano')

    if (intentos == numero_intentos) and (numero != meta):
        volver_jugar('perdio')

if __name__ == '__main__':
    adivina()
