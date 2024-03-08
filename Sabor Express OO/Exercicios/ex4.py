'''Agora é sua vez! Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. 
Adicione um método especial __str__ para imprimir uma representação em string da pessoa. 
Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. 
Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.'''

class Pessoa:
    def __init__(self, nome, idade, profissão='') -> None:
        self.nome = nome
        self.idade = idade
        self.profissão = profissão

    def __str__(self) -> str:
        return f'{self.nome} | {self.idade} | {self.profissão}'
    
    def aniversario(self):
        self.idade += 1
    
    @property
    def saudacao(self):
        if self.profissão:
            return f'Ola sou {self.nome}! Trabalho como {self.profissão}'
        else:
            return f'Ola sou {self.nome}'

pessoa1 = Pessoa('Lucas', 25, 'Programador')
pessoa2 = Pessoa('Giovana', 24)
pessoa1.aniversario()

print(pessoa1)
print(pessoa2)
print(pessoa2.saudacao)
print(pessoa1.saudacao)