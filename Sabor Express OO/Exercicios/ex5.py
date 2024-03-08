'''1 - Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. 
Inicie o atributo ativo como False por padrão.

2 - Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. 
Crie duas instâncias da classe e imprima essas instâncias.

3 - Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True.
 Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

4 - Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

5 - Crie uma instância da classe e imprima o valor da propriedade titular.

6 - Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos.
 Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

7 - Crie um método de classe para a conta ClienteBanco'''

class ContaBancaria:
    def __init__(self, titular, saldo) -> None:
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self) -> str:
        return f'Titular: {self.titular} | Saldo: R${self.saldo}'
    
    @classmethod
    def ativar_conta(cls,conta):
        conta._ativo = not conta._ativo
        return 'Ativo' if conta._ativo else 'Inativo'
    

conta_lucas = ContaBancaria('Lucas', 540.59)
conta_giovana = ContaBancaria('Giovana', 699.99)

print(conta_lucas)
print(ContaBancaria.ativar_conta(conta_lucas))
print(conta_giovana)

