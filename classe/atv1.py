class Pessoa:
    def __init__(self,nome,peso,idade,comendo=False,):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=comendo

    def comer(self,alimento):
        self.alimento=alimento
        print(f"{self.nome} está comendo{self.alimento}")




p1 = Pessoa("joão",80,19)
p2 = Pessoa("Marta",56,22,comendo=True)

p2.comer(" pipoca")


#print(vars(p2))
#print(p1.nome)