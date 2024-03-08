"""
Construa um código que calcule a média dos valores em uma lista.
Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
"""

lista = []

soma_da_lista = sum(lista)

try:
    print(f'A soma dos valores da lista é igual a: {soma_da_lista}\nE a média é igual a: {(soma_da_lista/len(lista))}')
except:
    print('Não é possivel calcular a média pois a lista esta vazia')