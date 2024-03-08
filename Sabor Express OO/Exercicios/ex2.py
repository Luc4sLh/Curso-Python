''''Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
    Crie uma instância dessa classe e atribua valores aos seus atributos.'''

class Carro:
    carros = []
    def __init__(self, modelo, cor, ano) -> None:
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.carros.append(self) 

    def __str__(self) -> str:
        return f'{self.modelo} | {self.cor} | {self.ano}'
    
    def listar_carros():
        for carro in Carro.carros:
            print(f'{carro.modelo} | {carro.cor} | {carro.ano}')

carro1 = Carro('Sedan', 'Preto', 2018)
carro2 = Carro('Hetch', 'Vermelho', 2015)
carro3 = Carro('SUV', 'Branco', 2022)
carro4 = Carro('Pickup', 'Prata', 2010)
carro5 = Carro('Variant', 'Azul', 1999)

Carro.listar_carros()