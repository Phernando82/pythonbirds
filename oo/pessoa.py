class Pessoa:
    def cumprimentar(self):
        return f'Hola! {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(p.cumprimentar())
    print(id(p))

