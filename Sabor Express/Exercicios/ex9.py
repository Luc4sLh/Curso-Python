"""
Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual.
"""

lista_de_numeros = []
for n in range(1, 11):
    lista_de_numeros.append(n)

lista_de_nomes = ['Lucas', 'Giovana', 'Isabella', 'Henrique']

lista_ano = [1999,2024]

print(f'{lista_de_numeros}\n{lista_de_nomes}\n{lista_ano}')