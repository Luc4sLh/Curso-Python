"""Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar,
se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você."""

usuario = 'Lucashsilva'
senha = 'MasterofCorte'

user_input = str(input('Login: '))
password_input = str(input('Senha: '))

if user_input == usuario and password_input == senha:
    print('Login feito com sucesso!')
else:
    print('Seu usuario ou senha estão incorretos, tente novamente.')