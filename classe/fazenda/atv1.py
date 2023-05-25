class Pessoa:
    def __init__(self,nome,peso,idade,comendo=False,andar=False,falar=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=False
        self.andando=andar
        self.falando=falar
''
    def comer(self,alimento):
        self.alimento=alimento
        if self.comendo==False:
            print(f"{self.nome} está comendo{self.alimento}")
            self.comendo=True

        else:
            print(f"{self.nome} já está comendo")

    def paradecomer(self):
        if self.comendo==True:
            print(f"{self.nome} parou de comer")
            self.comendo=False
        else:
            print(f"{self.nome} não está comendo")


    def falar(self):
        if self.falando==True:
            print(f"{self.nome}já está falando")

        elif self.comendo==True:
            print(f"{self.nome} Não pode falar pois está comendo")
        else:
            self.falando = True
            print(f"{self.nome} começou á falar")

    def paradefalar(self):
        if self.falar==True:
            print(f"{self.nome}parou de falar")
            self.falar=False
        else:
            print(f"{self.nome} não está falando")



    def andar(self):
        if self.andando == False:
            print(f"{self.nome} começou a andar")
            self.andando = True

        else:
            print(f"{self.nome} continuou a andar")

    def paradeandar(self):
        if self.andando == True:
            print(f"{self.nome} parou de andar")
            self.andando = False
        else:
            print(f"{self.nome} não esta andando")



p1 = Pessoa("joão",80,19)
p2 = Pessoa("Marta",56,22,comendo=True)

p2.comer(" pipoca")
p2.paradecomer()
p2.comer(" pão")
p2.falar()
p2.paradefalar()
p2.andar()
p2.paradeandar()



#print(vars(p2))
#print(p1.nome)