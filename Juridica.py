from Pessoa import Pessoa

class Juridica(Pessoa):

    def __init__(self, nomeJ, foneJ, cnpjJ):
        super().__init__(nomeJ, foneJ)
        self.cnpj = cnpjJ
    
    def imprimir(self):
        super().imprimir()
        print( "CNPF: ", self.cnpj)
        