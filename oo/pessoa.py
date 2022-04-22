class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Hola! {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass


if __name__ == '__main__':
    fernando = Homem(nome='Fernando')
    rubens = Homem(fernando, nome='Rubens')
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
    print(Pessoa.metodo_estatico(), rubens.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), rubens.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(fernando, Pessoa))
    print(isinstance(fernando, Homem))

