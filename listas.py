numeros = [1, 'Mario', True, 4.2, 5]
#Metodos mutables y estaticos de la clase 'list'
numeros.append(6)#Agrega un elemento al final

numeros.pop()
numeros.pop(1) #Elimina el elemento de la posicion 1
numeros.pop() #Elimina el ultimo elemento
eliminado = numeros.pop() #Devuleve el valor eliminado
print(numeros)
print(eliminado)
#[::] slice