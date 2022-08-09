#Funciones anonimas o lambda function
#Solo pueden tener una linea de codigo

palindromo = lambda palabra: palabra == palabra[::-1]

print(palindromo('ana'))
