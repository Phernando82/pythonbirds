class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Hola! {id(self)}'


if __name__ == '__main__':
    fernando = Pessoa(nome='Fernando')
    rubens = Pessoa(fernando, nome='Rubens')
    print(Pessoa.cumprimentar(rubens))
    print(rubens.cumprimentar())
    print(id(rubens))
    print(rubens.nome)
    rubens.nome = 'Fernando'
    print(rubens.nome)
    print(rubens.idade)
    print(rubens.filhos)
