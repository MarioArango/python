DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]
#HOF -> lista de disccionarios
all_python_devs = list(filter(lambda item: item['language'] == 'python' , DATA))
#camprejenshions -> directo al nombre
all_python_devs = [item['name'] for item in DATA if item['language']=='python']
# print(all_python_devs)


all_platzi_workers = list(filter(lambda item: item['organization'] == 'Platzi' , DATA))
all_platzi_workers = [item['name'] for item in DATA if item['organization'] == 'Platzi']
# print(all_platzi_workers)


all_adults = list(filter(lambda item: item['age'] > 18 , DATA))
all_adults = list(map(lambda item: item['name'] , all_adults))
#Si se quiere obtener una lista directa de valores, es mejor usar compren.., porque el otro
#requiere 2 HOF, filter y map
# print(all_adults)

#El simbolo pai | une el item con lo que sigue, agrega keys nuevos a cada item del dict
old_people = list(map(lambda worker: worker | {'old': worker['age']>70}, DATA))
print(old_people)
