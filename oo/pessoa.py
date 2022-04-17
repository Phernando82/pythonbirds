class Pessoa:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Hola! {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Rubens')
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(id(p))
    print(p.nome)
    p.nome = 'Fernando'
    print(p.nome)
    print(p.idade)
