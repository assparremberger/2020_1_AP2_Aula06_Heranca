from Pessoa import Pessoa

class Fisica(Pessoa):

    def __init__(self, nomeF, foneF, cpfF):
        Pessoa.__init__(self,nomeF, foneF)
        self.cpf = cpfF

    def imprimir(self):
        Pessoa.imprimir(self)
        print( "CPF: ", self.cpf)