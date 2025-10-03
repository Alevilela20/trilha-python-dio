frutas = ["laranja", "maca", "uva"]
print(frutas)

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)



frutas2 = ["maçã", "laranja", "uva", "pera"]
print(frutas2[-1])

carros = ["gol", "celta", "palio"]
for carro in carros:
    print(carro)

numeros = [1,30,21,2,9,65,34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)


quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)

print (quadrado)