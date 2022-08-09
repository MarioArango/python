    # list_numeros_cuadrados = []

    # for numero in range(1, 101):
    #     if numero%3 != 0:
    #         list_numeros_cuadrados.append(numero**2)

    # print(list_numeros_cuadrados)


list_numeros_cuadrados = [numero**2 for numero in range(1, 101) if numero%3 != 0]
list_multiplos = [numero for numero in range(1, 100001) if numero%36 == 0]

# print(list_numeros_cuadrados)
print(list_multiplos)