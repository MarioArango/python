#Pertence a la clase dict
persona = {
    'nombre': 'Mario',
    'apellido': 'Arango',
    'edad': 26
}
#Se accede con corchetes y no con punto, porque las keys no son variables
# print(persona['nombre'])

for item in persona.keys():
    print(item)

for item in persona.values():
    print(item)

for key, value in persona.items():
    print(key)
    print(value)