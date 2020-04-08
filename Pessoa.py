class Pessoa:

    def __init__(self, nomeP, foneP):
        self.nome = nomeP
        self.fone = foneP

    def imprimir(self):
        print( "Nome: ", self.nome)
        print( "Fone: ", self.fone)
