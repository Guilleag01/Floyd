from copy import deepcopy
import re
from termcolor import colored, cprint


def introducirDatos():
    text = ""
    size = 100
    while size > 26:
        size = int(input("Introduce el número de nodos del grafo: "))
        if size > 26:
            print("El número máximo de nodos es 26 (por el número de letras)")

    G = [[0 for a in range(size)] for b in range(size)]
    printMatriz(G)

    abcd = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while(text != "STOP"):
        text = input("Introduce la relación: ([from][to] [cost]): ")
        text = text.upper()
        if re.match("[A-Z][A-Z] [0-9][0-9]?$", text):
            fr = abcd.find(text[0])
            to = abcd.find(text[1])
            if fr < size and to < size:
                value = int(text[3:])
                G[fr][to] = value
                printMatriz(G)
            else:
                print("La entrada no es correcta")
        else:
            if text != "STOP":
                print("La entrada no es correcta")
    for a in range(size):
        for b in range(size):
            if G[a][b] == 0:
                G[a][b] = 100
    
    return G

def printMatriz(matriz:list, ii = -1, jj = -1):
    size = len(matriz)
    print("") 
    abcd = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print("  ", end="")
    for i in range(size):
        print("  " + abcd[i], end="")
    print("")
    for i in range(size):
        print(abcd[i] + " ", end="")
        for j in range(size):
            if type(matriz[i][j]) == int:
                if matriz[i][j] == 0 or matriz[i][j] > 99 or i == j:
                    print("   ", end="")
                else:
                    if i == ii and j == jj:
                        cprint(" {:02d}".format(matriz[i][j]), 'grey', 'on_white', end="")
                    else:
                        print(" {:02d}".format(matriz[i][j]), end="")
            else:
                if matriz[i][j] == 0 or i == j:
                    print("   ", end="")
                else:
                    print("  " + matriz[i][j], end="")
        print("")
    print("")

def main():
    abcd = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    G = introducirDatos()778
    D = deepcopy(G)
    printMatriz(D)
    n = len(G)
    P = [[0 for a in range(n)] for b in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j] > D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    P[i][j] = abcd[k]
                    print("\nNODO INTERMEDIO " + abcd[k])
                    printMatriz(D, i, j)
                    printMatriz(P, i, j)
    print("")
    print("Matriz adyacencia")
    printMatriz(G)
    print("Matriz distancias mínimas")
    printMatriz(D)
    print("Matriz caminos mínimos")
    printMatriz(P)
    


if __name__ == "__main__":
    main()