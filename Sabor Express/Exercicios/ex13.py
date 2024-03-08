"""Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10."""

numero_do_usuario = int(input('Escolha um numero para ver a sua tabuada: '))

for n in range(1,11):
    print(f'{numero_do_usuario} X {n} = {n*numero_do_usuario}')