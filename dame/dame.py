from copy import deepcopy
from Figura import *
import math
from Tree import *
from TreeNode import *
from Provera import *
from MinMaxAlg import *



def napraviCrne():
    crni=[]
    for i in range(1,9):
        if i%2==1:
            f = Figura(7, i)
            crni.append(f)
        else:
            f1 = Figura(6, i)
            f2 = Figura(8, i)
            crni.append(f1)
            crni.append(f2)
    return crni

def napraviBele():
    beli = []
    for i in range(1, 9):
        if i % 2 == 1:
            f1 = Figura(1, i)
            f2 = Figura(3, i)
            beli.append(f1)
            beli.append(f2)
        else:
            f = Figura(2, i)
            beli.append(f)

    return beli

def prikaziTablu(crni,beli):
    for i in range(1,9):
        for j in range(1,9):
            if daLiJePoljeZauzeto(crni,i,j):
                indx=nadjiFiguru(crni,i,j)
                if crni[indx].daLiJeDama()==False:
                    print("x",end="     ")
                else:
                    print("X", end="     ")

            elif daLiJePoljeZauzeto(beli,i,j):
                indx=nadjiFiguru(beli,i,j)
                if beli[indx].daLiJeDama()==False:
                    print("o", end="     ")
                else:
                    print("O", end="     ")

            else:
                print("-",end="     ")

        print("\n")

def pomeriSeCovek(black,white):
    x=int(input("Unesite red na kom se nalazi figura \n"))
    y=int(input("Unesite kolonu u kojoj se nalazi figura\n"))
    if nadjiFiguru(black,x,y)==False:
        print("Ne postoji figura na unetoj poziciji")
        return False
    else:
        index=nadjiFiguru(black,x,y)
        newX=int(input("Unesite  red na koje zelite da stavite figuru\n"))
        newY=int(input("Unesite  kolonu  na koju zelite da stavite figuru\n"))
        if(daLiJePotezMoguc(black[index],newX,newY,black,white)):
            if black[index].daLiJeDama() == False:
                if black[index].getX()-newX==2 and abs(newY-black[index].getY())==2:
                    if newY>black[index].getY():
                        move=1
                    else:
                        move=-1
                    indx=nadjiFiguru(white,black[index].getX()-1,black[index].getY()+move)
                    if opcija==1:
                        opc=input("Da li zelite zelite da pojedete protivnicku figuru [da,ne]\n")
                        if opc=="da":
                            white.pop(indx)
                    else:
                        white.pop(indx)
                    black[index].move(newX,newY)
                    if black[index].getY()==1:
                        black[index].postaniDama()
                    print("Black from " + str(black[index].getX()) + "," + str(black[index].getY()) + " to: " + str(
                        newX) + "," + str(newY))
                    return True
            elif abs(black[index].getX() - newX) == 2 and abs(newY - black[index].getY()) == 2:
                if newY>black[index].getY():
                    moveY=1
                else:
                    moveY=-1
                if newX>black[index].getX():
                    moveX=1
                else:
                    moveX=-1
                indx=nadjiFiguru(white,black[index].getX()+moveX,black[index].getY()+moveY)
                print("Black from " + str(black[index].getX()) + "," + str(black[index].getY()) + " to: " + str(
                    newX) + "," + str(newY))
                black[index].move(newX, newY)
                if black[index].getY() == 1:
                    black[index].postaniDama()

                white.pop(indx)
                return True


            print("Black from " + str(black[index].getX()) + "," + str(black[index].getY()) + " to: " + str(
                newX) + "," + str(newY))
            black[index].move(newX, newY)
            if newX==1:
                black[index].postaniDama()
            return  True
        else:
            print("Nije moguce odigrati trazeni potez")
            return False



def KreirajStabloIgre(cvor,dubina):
    if stabloIgre.depth(cvor)<dubina:
        allPossibleStates=mogucaStanjaIgre(cvor)
        for state in allPossibleStates:
            child=TreeNode(state)
            cvor.add_child(child)
        for child in cvor.children:
            KreirajStabloIgre(child,dubina)








Beli=napraviBele()
Crni=napraviCrne()

tabla={"beli":Beli,"crni":Crni,"AI":True}

opcija=int(input("1. Normalan rezim rada \n2. Rezim u kom je obavezno pojesti\n"))

while True:
        koren=TreeNode(tabla)
        stabloIgre=Tree()
        stabloIgre.root=koren
        KreirajStabloIgre(koren,3)
        izracunajZaListove(koren)
        MiniMax(koren)
        for dete in koren.children:
            if koren.score==dete.score:
                tabla=dete.data

        prikaziTablu(tabla["crni"],tabla["beli"])
        print("=========================================")
        if len(tabla["crni"])==0:
            print("Pobenik je kompjuter")
            break

        while pomeriSeCovek(tabla["crni"],tabla["beli"])==False:
            if pomeriSeCovek(tabla["crni"], tabla["beli"])==True:
                break


        prikaziTablu(tabla["crni"],tabla["beli"])
        print("=========================================")

        noviCrni=deepcopy(tabla["crni"])
        noviBeli=deepcopy(tabla["beli"])
        novaTabla={"crni":noviCrni,"beli":noviBeli,"AI":True}
        tabla=novaTabla
        if len(tabla["beli"])==0:
            print("Pobenik je covek")
            break
