#Pertenece a la clase 'range', para usarlo debemos parsearlo a una lista
#lista = list(range(1, 100, 10)) # limite superios no inclusivo 
#lista = list(range(1, 100))# salta de 1 en uno
lista = list(range(100))#inicia en 0, salta de 1 en uno
for item in lista: #puede ir una list o un range y python lo parsea a lista
    print(item)

#continue, salta al siguiente ciclo, no ejecuta lo que este debajo
#break, sale del ciclo for, no ejecuta lo que esta debajo al salir
#ambos son validos para while y for

for numero in range(100):
    #numero%x = 0 si es multiplo de x
    #numero%x != 0 si no es multiplo de x
    #numero%x = r si es multiplo de x + r, has esto
    if numero%2!=0:
        continue
    else:
        print(numero)