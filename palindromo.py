def palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    if palabra == palabra[::-1]:
        print('Es un palindromo')
    else:
        print('No es un palindromo')

#Entrada de ejecucion
#Cuando se ejecuta, iniciara compilando todo lo que esta debajo
if __name__ == '__main__':
    palabra = input('Ingrese una palabra: ')
    palindromo(palabra)