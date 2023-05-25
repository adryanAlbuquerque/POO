class Animal:
    def _init_(self,nome,cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f'{self.nome} comendo ')