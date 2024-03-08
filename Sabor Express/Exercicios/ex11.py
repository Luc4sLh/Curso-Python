"""Utilize um loop for para calcular a soma dos números ímpares de 1 a 10."""

pares = []
impares = []

for numero in range(1,11):
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f'Os numeros pares de 1 a 10 são:{pares}\nE os numeros impares são:{impares}')
print(f'A soma dos numeros impares de 1 a 10 é igual a {sum(impares)}')
