#Suelen usarse dentro de Funciones de orden superior, las cuales
#son funciones que reciben como parametro otra funcion, esta funcion
#suele no necesitar un identificar, solo una ejecucion, por eso
#van las lambda function

from functools import reduce

my_list = [1,4,5,6,9,13,19,21]

#Genera un iterador, por eso debe parseado
my_new_list_filter = list(filter(lambda item: item%2 == 0, my_list))
# print(my_new_list_filter)

my_new_list_map = list(map(lambda item: item**2, my_list))
# print(my_new_list_map)
#a: es el primer numero de la lista
#b: es el segundo numero de la lista
#No necesita ser parsea a un list, poruqe retorna directo un numero
my_new_list_reduce = reduce(lambda a,b: a + b, my_list)
print(my_new_list_reduce)
