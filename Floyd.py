from copy import deepcopy
import re


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

    while(text != "stop"):
        text = input("Introduce la relación: ([from][to] [cost]): ")
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
            if text != "stop":
                print("La entrada no es correcta")
    
    return G

def printMatriz(matriz:list):
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
            print(" {:02d}".format(matriz[i][j]), end="")
        print("")
    print("")

def main():
    G = introducirDatos()
    D = deepcopy(G)
    printMatriz(D)
    P = []


if __name__ == "__main__":
    main()