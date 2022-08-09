# dic_cubos = {}

# for numero in range(1, 101):
#     dic_cubos[numero] = numero**3

# print(dic_cubos)

dic_cubos = {numero: numero**3 for numero in range(1, 101) if numero%3 != 0}
dic_raices = {numero: numero**0.5 for numero in range(1, 1001)}

print(dic_cubos)
print(dic_raices)