from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica



p = Pessoa("Joao", "1234")
f = Fisica("Maria", "2222", "111")

p.imprimir()
print("-------")
f.imprimir()
print("-------")
j = Juridica("Senac", "33224455", "01.235")
j.imprimir()