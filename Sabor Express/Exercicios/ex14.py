"""
Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
Utilize um bloco try-except para lidar com possíveis exceções.
"""

lista = [7,9,3,5.8,15,3,'5']
soma = 0

for n in lista:
    try:
        soma += n
    except:
        print(f'O valor {n} na posição {lista.index(n)} da lista não é do tipo int ou float, e sim {type(n)}, por favor verifique a lista novamente')
print(soma)