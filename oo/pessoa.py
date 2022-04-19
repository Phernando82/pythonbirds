class Pessoa:
    olhos = 2
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
    print(id(rubens))
    print(rubens.cumprimentar())
    print(rubens.nome)
    print(rubens.idade)
    for filho in rubens.filhos:
        print(filho.nome)
    rubens.sobrenome = 'Ramalho'
    print(rubens.filhos)
    del rubens.filhos
    rubens.olhos = 1
    del rubens.olhos
    print(fernando.__init__)
    print(rubens.__init__)
    print(Pessoa.olhos)
    print(rubens.olhos)
    print(fernando.olhos)
    print(id(Pessoa.olhos), id(rubens.olhos), id(fernando.olhos))

