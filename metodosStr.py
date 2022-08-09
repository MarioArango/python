nombre = 'mario '
#Metodos inmutables
#METODOS ESTATICOS DE LA CLASE STR
#Transforma a mayuscula
print(nombre.upper())
#Transforma en oracion
print(nombre.capitalize())
#Quita los espacios vacios de los extremos
print(nombre.strip())
#Transforma a minuscula
print(nombre.lower())
#Reemplaza el primer caracter del primer parametro por el segundo
print(nombre.replace('o', 'o Jesús'))
#Extrae un caracter, ya que un str es una lista de caracteres
print(nombre[0])
#METODO GLOBAL
#Calcula la cantidad de caracteres
print(len(nombre))
#No inclusivo inferiormente, trae los caracteres mayores al primero
print(nombre[1:len(nombre)])
print(nombre[::-1])

