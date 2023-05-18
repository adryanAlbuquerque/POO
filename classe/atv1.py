class Pessoa:
    def __init__(self,nome,peso,idade,comendo=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=comendo

p1 = Pessoa("joão",80,19)
p2 = Pessoa("Marta",56,22,comendo=True)
print(vars(p2))
print(vars(p1))