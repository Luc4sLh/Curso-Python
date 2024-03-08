class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao) -> None:
        self.nome = nome
        self.artista = artista
        self.duracao = int(duracao)
        self.musicas.append(self)

    def __str__(self) -> str:
        return f'{Musica.nome} | {Musica.artista} | {Musica.duracao}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'''Nome: {musica.nome} | Artista: {musica.artista} | Duração: {musica.duracao} minutos''')
    

musica1 = Musica('New Divide', 'Linkin Park', 3)
musica2 = Musica('Like a Stone', 'Audioslave', 4)
musica3 = Musica('Chop Suey', 'System of a Down', 4)
musica4 = Musica('Bohemian Rapsody', 'Queen', 7)
musica5 = Musica('Nutshell', 'Alice in Chains', 2.5)

Musica.listar_musicas()