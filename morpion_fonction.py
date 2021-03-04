import sys

def numero_case(j) :
    print(" ")
    print("C'est le tour du joueur", j)
    case=str(input("Entrez la case : "))
    print("Vous avez joué la case", case)
    return case

def grille(L) :
    print(" ")
    print("    0   1   2")
    print("  -------------")
    for i in range(3):
        print(chr(65+i), "|", L[i][0], "|", L[i][1], "|", L[i][2], "|")
        print("  -------------")

def place_pion(L) :
    symbole=" XO"
    case=numero_case(i)
    assert case[0]=="A" or case[0]=="B" or case[0]=="C"
    colonne=int(case[1])
    if case[0]=="A" :
        assert L[0][colonne]==" "
        L[0][colonne]=symbole[i]
    elif case[0]=="B" :
        assert L[1][colonne]==" "
        L[1][colonne]=symbole[i]
    elif case[0]=="C" :
        assert L[2][colonne]==" "
        L[2][colonne]=symbole[i]
        
def symboles_alignés(L):
    for i in range(3):
        if L[i][0]==L[i][1]==L[i][2]:
            return L[i][0]
            break
        elif L[0][i]==L[1][i]==L[2][i]:
            return L[0][i]
            break
    if L[0][0]==L[1][1]==L[2][2] or L[0][2]==L[1][1]==L[2][0]:
        return L[1][1]

L=[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

for k in range (9):
    if k%2==0:
        i=1
    else:
        i=2
    grille(L)
    place_pion(L)
    if symboles_alignés(L)=="X":
        grille(L)
        print(" ")
        print("Le joueur 1 a gagné !")
        sys.exit(0)
    elif symboles_alignés(L)=="O":
        grille(L)
        print(" ")
        print("Le joueur 2 a gagné !")
        sys.exit(0)
grille(L)
print(" ")
print("Match nul !")
