soles = float(input('¿Cuántos soles tienes?: '))
valor_dolar = 4.1
dolares = soles/valor_dolar
dolares = round(dolares, 2)
#Lo parsea a str, porque en el print se puede concatenar entre cadenas
dolares = str(dolares)
print(f'Tienes ${dolares} dolares')

dol = float(input('¿Cuántos dolares tienes?: '))
val_dol = 4.1
sol = dol*val_dol
sol = round(sol, 2)
sol = str(sol)
print(f'Tienes ${sol} nuevos soles')


