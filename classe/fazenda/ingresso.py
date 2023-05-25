class Ingresso:
    def __init__(self, reais):
        self.reais = reais

    def ValorAdd(self):
        print(f'{self.reais}')

class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor)

    def ValorAdd(self, valorAdicional):
        self.valorAdicional = valorAdicional
        self.reais += self.valorAdicional
        print(f'{self.reais}')

ingresso = Ingresso(10)
vip = Vip(25)
ingresso.ValorAdd()
vip.ValorAdd(15)
