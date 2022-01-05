import random
import os

class Jogador:
    def __init__(self, nome):
        self.nome = nome


class Jogo:
    def __init__(self, jogador, tab):
        self.tab = [["*","*","*"],["*","*","*"], ["*","*","*"]]
        self.jogador = jogador
        self.rodada = 0
    
    def imprimirTabuleiro(self):
        for i in range(len(self.tab)):
            print(*self.tab[i])
    
    def realizarJogada(self):          
        lin = int(input("Indique a linha: "))
        col = int(input("Indique a coluna: "))
        if self.verificarVazios(lin, col) == True:
            self.tab[lin][col] = "X"
            self.rodada += 1
        else:
            while self.verificarVazios(lin, col) == False:
                lin = int(input("Espaço ocupado. Indique outra linha: "))
                col = int(input("Espaço ocupado. Indique outra coluna: "))
                if self.verificarVazios(lin, col) == True:
                    self.tab[lin][col] = "X"
                    self.rodada += 1
                    break

    def verificarVazios(self, lin, col):
        if self.tab[lin][col] == "*":
            return True
        else:
            return False
    
    def IA(self):
        list_moves = []
        for i in range(3):
            for j in range(3):
                if self.tab[i][j] == "*":
                    list_moves.append((i, j))
        
        if len(list_moves) > 0:
            x, y = random.choice(list_moves)
            self.tab[x][y] = "O"

    
    def verificarVitoria(self):
        if ((self.tab[0][0] == "X" and self.tab[1][1] == "X" and self.tab[2][2] == "X") or #diagonalprincipal
        (self.tab[0][0] == "X" and self.tab[0][1] == "X" and self.tab[0][2] == "X") or #linha0
        (self.tab[0][0] == "X" and self.tab[1][0] == "X" and self.tab[2][0] == "X") or #coluna0
        (self.tab[0][1] == "X" and self.tab[1][1] == "X" and self.tab[2][1] == "X") or #coluna1
        (self.tab[0][2] == "X" and self.tab[1][2] == "X" and self.tab[2][2] == "X") or #coluna2
        (self.tab[1][0] == "X" and self.tab[1][1] == "X" and self.tab[1][2] == "X") or #linha1
        (self.tab[2][0] == "X" and self.tab[2][1] == "X" and self.tab[2][2] == "X") or #linha2
        (self.tab[2][0] == "X" and self.tab[1][1] == "X" and self.tab[0][2] == "X")): #diagonalsecundaria
            return 1
        elif ((self.tab[0][0] == "O" and self.tab[1][1] == "O" and self.tab[2][2] == "O") or #diagonalprincipal
        (self.tab[0][0] == "O" and self.tab[0][1] == "O" and self.tab[0][2] == "O") or #linha0
        (self.tab[0][0] == "O" and self.tab[1][0] == "O" and self.tab[2][0] == "O") or #coluna0
        (self.tab[0][1] == "O" and self.tab[1][1] == "O" and self.tab[2][1] == "O") or #coluna1
        (self.tab[0][2] == "O" and self.tab[1][2] == "O" and self.tab[2][2] == "O") or #coluna2
        (self.tab[1][0] == "O" and self.tab[1][1] == "O" and self.tab[1][2] == "O") or #linha1
        (self.tab[2][0] == "O" and self.tab[2][1] == "O" and self.tab[2][2] == "O") or #linha2
        (self.tab[2][0] == "O" and self.tab[1][1] == "O" and self.tab[0][2] == "O")):
            return 2
        
        else: 
            cont  = 0
            for i in range(3):
                for j in range(3):
                    if self.tab[i][j] == "*":
                        cont += 1
                        return 0
            if cont == 0:
                return 3





tab = []
player = Jogador("Eldio")
game = Jogo(player, tab)

while game.verificarVitoria() == 0:
    os.system("cls")
    game.imprimirTabuleiro()
    game.realizarJogada()
    game.IA()
    if game.verificarVitoria() == 1:
        print("Jogador 1 venceu.")
        break
    elif game.verificarVitoria() == 2:
        print ("IA venceu")
        break
    elif game.verificarVitoria() == 3:
        print("Empate")
        break