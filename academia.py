import random

class Academia:
    def __init__(self):
        self.halteres = [i for i in range(10, 36) if i % 2 == 0]
        self.porta_halteres = {}
        self.reiniciarDia()
    
    def reiniciarDia(self):
        self.porta_halteres = {i: i for i in self.halteres}
    
    def listarHalteres(self):
        return [i for i in self.porta_halteres.values() if i != 0]
    
    def listarEspacos(self):
        return [i for i, j in self.porta_halteres.items() if j == 0]

    def pegarHaltere(self, peso):
        halt_pos = list(self.porta_halteres.values()).index(peso)
        key_halt = list(self.porta_halteres.keys())[halt_pos]

        self.porta_halteres[key_halt] = 0

        return peso
    
    def devolverHalter(self, pos, peso):
        self.porta_halteres[pos] = peso
    
    def calcularCaos(self):
        num_caos = [i for i, j in self.porta_halteres.items() if i != j]
        return len(num_caos)/len(self.porta_halteres)


class Usuario:
    def __init__(self, tipo, academia):
        self.tipo = tipo #tipo 1 = normal, tipo 2 = bagunceiro
        self.academia = academia
        self.peso = 0

    def iniciarTreino(self):
        listaPesos = self.academia.listarHalteres()
        self.peso = random.choice(listaPesos)
        self.academia.pegarHaltere(self.peso)

    def finalizarTreino(self):
        espaco = self.academia.listarEspacos()
        
        if self.tipo == 1:
            if self.peso in espaco:
                self.academia.devolverHalter(self.peso, self.peso)
            else:                
                pos = random.choice(espaco)
                self.academia.devolverHalter(pos, self.peso)
        
        if self.tipo == 2:
            pos = random.choice(espaco)
            self.academia.devolverHalter(pos, self.peso)
        
        self.peso = 0

academia = Academia()
usuarios = [Usuario(1, academia) for i in range(10)]
usuarios += [Usuario(2, academia) for i in range(1)]

random.shuffle(usuarios)
list_caos = []
for k in range(50):
    academia.reiniciarDia()
    for i in range (10):
        random.shuffle(usuarios)
        for user in usuarios:
            user.iniciarTreino()
        for user in usuarios:
            user.finalizarTreino()
    list_caos += [academia.calcularCaos]

import seaborn as sns
sns.displot(list_caos)