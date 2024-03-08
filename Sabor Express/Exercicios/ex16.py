'''Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.'''
informacoes_usuario = {'nome' : 'Lucas', 'idade': 25, 'cidade' : 'Apucarana'}
 

'''Utilizando o dicionário criado no item 1:

    Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
    Adicione um campo de profissão para essa pessoa;
    Remova um item do dicionário.'''

informacoes_usuario['idade'] = 65
informacoes_usuario['profissao'] = 'Cortador'
informacoes_usuario.pop('cidade')
print(informacoes_usuario) 