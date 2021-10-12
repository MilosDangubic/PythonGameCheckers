from copy import deepcopy

def nadjiFiguru(figure,x,y):
    for i in range(len(figure)):
        if figure[i].getX()==x and figure[i].getY()==y:
            return i
    return  -1
def daLiJePoljeZauzeto(figure,x,y):
    for figura in figure:
        if figura.getX()==x and figura.getY()==y:
            return True
    return False

def daLiJePotezMoguc(figure,newX,newY,black,white):
    if daLiJePoljeZauzeto(black,newX,newY)==False and daLiJePoljeZauzeto(white,newX,newY)==False and newY>0 and newX>0 and newY<9 and newX<9:
        if figure.getTip()=="obican":
            if figure.getX()-newX==1 and abs(newY-figure.getY())==1:
                return True
            elif figure.getX()-newX==2 and abs(newY-figure.getY())==2:
                if newY>figure.getY():
                    move=1
                else:
                    move=-1
                if daLiJePoljeZauzeto(white,figure.getX()-1,figure.getY()+move)==True:
                    return True
                else:
                    return False

            else:
                return False
        elif figure.getTip()=="dama":
            if abs(figure.getX()-newX)==1 and abs(newY-figure.getY())==1:
                return True
            elif abs(figure.getX()-newX)==2 and abs(newY-figure.getY())==2:
                if newY>figure.getY():
                    moveY=1
                else:
                    moveY=-1
                if newX>figure.getX():
                    moveX=1
                else:
                    moveX=-1

                if daLiJePoljeZauzeto(white,figure.getX()+moveX,figure.getY()+moveY)==True:
                    return True
                else:
                    return False
            else:
                return False
    else:
            return False


def daLiJePotezMogucAI(figure,newX,newY,black,white):
    if figure.getTip()=="obican":
        if daLiJePoljeZauzeto(black,newX,newY)==False and daLiJePoljeZauzeto(white,newX,newY)==False and newY>0 and newX>0 and newY<9 and newX<9:
            if newX-figure.getX()==1 and abs(newY-figure.getY())==1:
                return True
            elif newX-figure.getX()==2 and abs(newY-figure.getY())==2:
                if newY>figure.getY():
                    move=1
                else:
                    move=-1
                if daLiJePoljeZauzeto(black,figure.getX()+1,figure.getY()+move)==True:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    elif figure.getTip()=="dama"  and daLiJePoljeZauzeto(black,newX,newY)==False and daLiJePoljeZauzeto(white,newX,newY)==False and newY>0 and newX>0 and newX<9 and newY<9:
        if abs(figure.getX()-newX)==1 and abs(newY-figure.getY())==1:
            return True
        elif abs(figure.getX()-newX)==2 and abs(newY-figure.getY())==2:
            if newY>figure.getY():
                moveY=1
            else:
                moveY=-1
            if newX>figure.getX():
                moveX=1
            else:
                moveX=-1

            if daLiJePoljeZauzeto(black,figure.getX()+moveX,figure.getY()+moveY)==True:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def mogucaStanjaIgre(cvor):
    possibleStates=[]
    stanjeTable=deepcopy(cvor.data)

    beli=deepcopy(stanjeTable["beli"])
    crni=deepcopy(stanjeTable["crni"])
    if stanjeTable["AI"]:
        for i in range(len(beli)):
            if beli[i].daLiJeDama() == False:
                j = 2
                possibleX = beli[i].getX() + 1
                possibleY = beli[i].getY() - 1

                while j > 0:
                    noviBeli = deepcopy(beli)
                    noviCrni = deepcopy(crni)
                    if daLiJePotezMogucAI(noviBeli[i], possibleX, possibleY,crni,beli):
                        noviBeli[i].move(possibleX, possibleY)
                        if noviBeli[i].getX() == 8:
                            noviBeli[i].postaniDama()
                        newState={"beli":noviBeli,"crni":noviCrni,"AI":not stanjeTable["AI"]}

                        possibleStates.append(newState)
                    j = j - 1
                    possibleY = possibleY + 2
                j = 2
                possibleX = beli[i].getX() + 2
                possibleY = beli[i].getY() -2
                while j > 0:
                    noviBeli = deepcopy(beli)
                    noviCrni=deepcopy(crni)
                    if daLiJePotezMogucAI(noviBeli[i], possibleX, possibleY,crni,beli):
                        if possibleY>noviBeli[i].getY():
                            move=1
                        else:
                            move=-1
                        indx=nadjiFiguru(noviCrni,noviBeli[i].getX()+1,noviBeli[i].getY()+move)
                        noviCrni.pop(indx)
                        noviBeli[i].move(possibleX, possibleY)
                        if noviBeli[i].getX() == 8:
                            noviBeli[i].postaniDama()
                        newState={"beli":noviBeli,"crni":noviCrni,"AI":not stanjeTable["AI"]}

                        possibleStates.append(newState)
                    j = j - 1
                    possibleY = possibleY + 4

            else:
                possibleX = beli[i].getX() - 1
                possibleY = beli[i].getY() - 1
                j = 2
                while j > 0:
                    noviBeli = deepcopy(beli)
                    noviCrni = deepcopy(crni)
                    if daLiJePotezMogucAI(noviBeli[i], possibleX, possibleY,crni,beli):
                        noviBeli[i].move(possibleX, possibleY)
                        if noviBeli[i].getX() == 8:
                            noviBeli[i].postaniDama()
                        newState={"beli":noviBeli,"crni":noviCrni,"AI":not stanjeTable["AI"]}
                        possibleStates.append(newState)
                    j = j - 1
                    possibleY = possibleY + 2

                possibleX = beli[i].getX() + 1
                possibleY = beli[i].getY() - 1
                j = 2
                while j > 0:
                    noviBeli = deepcopy(beli)
                    noviCrni = deepcopy(crni)
                    if daLiJePotezMogucAI(noviBeli[i], possibleX, possibleY,crni,beli):
                        noviBeli[i].move(possibleX, possibleY)
                        if noviBeli[i].getX() == 8:
                            noviBeli[i].postaniDama()
                        newState={"beli":noviBeli,"crni":noviCrni,"AI":not stanjeTable["AI"]}
                        possibleStates.append(newState)
                    j = j - 1
                    possibleY = possibleY + 2

                possibleX = beli[i].getX() + 2
                possibleY = beli[i].getY() - 2
                j = 2
                while j > 0:
                    noviBeli = deepcopy(beli)
                    noviCrni = deepcopy(crni)
                    if daLiJePotezMogucAI(noviBeli[i], possibleX, possibleY, crni, beli):
                        if noviBeli[i].getX()<possibleX:
                            searchX=1+noviBeli[i].getX()
                        else:
                            searchX=-1+noviBeli[i].getX()

                        if noviBeli[i].getY()<possibleY:
                            searchY=1+noviBeli[i].getY()
                        else:
                            searchY=-1+noviBeli[i].getY()

                        indx=nadjiFiguru(noviCrni,searchX,searchY)
                        noviCrni.pop(indx)
                        noviBeli[i].move(possibleX, possibleY)
                        newState = {"beli": noviBeli, "crni": noviCrni, "AI": not stanjeTable["AI"]}
                        possibleStates.append(newState)
                    j = j - 1
                    possibleY = possibleY + 4



                possibleX = beli[i].getX() -2
                possibleY = beli[i].getY() - 2
                j = 2
                while j > 0:
                    noviBeli = deepcopy(beli)
                    noviCrni = deepcopy(crni)
                    if daLiJePotezMogucAI(noviBeli[i], possibleX, possibleY, crni, beli):
                        if noviBeli[i].getX() < possibleX:
                            searchX = 1 + noviBeli[i].getX()
                        else:
                            searchX = -1 + noviBeli[i].getX()

                        if noviBeli[i].getY() < possibleY:
                            searchY = 1 + noviBeli[i].getY()
                        else:
                            searchY = -1 + noviBeli[i].getY()

                        indx = nadjiFiguru(noviCrni, searchX, searchY)
                        noviCrni.pop(indx)
                        noviBeli[i].move(possibleX, possibleY)
                        newState = {"beli": noviBeli, "crni": noviCrni,
                                        "AI": not stanjeTable["AI"]}
                        possibleStates.append(newState)
                    j = j - 1
                    possibleY = possibleY + 4
    else:
        for i in range(len(crni)):
            if crni[i].daLiJeDama() == False:
                j = 2
                possibleX = crni[i].getX() - 1
                possibleY = crni[i].getY() - 1
                while j > 0:
                    noviBeli = deepcopy(beli)
                    noviCrni = deepcopy(crni)
                    if daLiJePotezMoguc(noviCrni[i], possibleX, possibleY,crni,beli):
                        noviCrni[i].move(possibleX, possibleY)
                        if noviCrni[i].getX() == 8:
                            noviCrni[i].postaniDama()
                        newState = {"beli": noviBeli, "crni": noviCrni, "AI": not stanjeTable["AI"]}

                        possibleStates.append(newState)
                    j = j - 1
                    possibleY = possibleY + 2

                possibleX = crni[i].getX() - 2
                possibleY = crni[i].getY() - 2
                j=2
                while j > 0:
                    noviBeli = deepcopy(beli)
                    noviCrni = deepcopy(crni)
                    if daLiJePotezMoguc(noviCrni[i], possibleX, possibleY, crni, beli):
                        if noviCrni[i].getY()<possibleY:
                            searchY=1+noviCrni[i].getY()
                        else:
                            searchY=-1+noviCrni[i].getY()
                        indx=nadjiFiguru(beli,noviCrni[i].getX()-1,searchY)
                        noviBeli.pop(indx)
                        noviCrni[i].move(possibleX, possibleY)
                        if noviCrni[i].getX() == 8:
                            noviCrni[i].postaniDama()
                        newState = {"beli": noviBeli, "crni": noviCrni, "AI": not stanjeTable["AI"]}
                        possibleStates.append(newState)
                    j = j - 1
                    possibleY = possibleY + 4

            else:
                possibleX = crni[i].getX() - 1
                possibleY = crni[i].getY() - 1
                j = 2
                while j > 0:
                    noviCrni = deepcopy(crni)
                    noviBeli=deepcopy(beli)
                    if daLiJePotezMoguc(noviCrni[i], possibleX, possibleY,crni,beli):
                        noviCrni[i].move(possibleX, possibleY)
                        if noviCrni[i].getX() == 8:
                            noviCrni[i].postaniDama()
                        newState = {"beli": noviBeli, "crni": noviCrni, "AI": not stanjeTable["AI"]}
                        possibleStates.append(newState)
                    j = j - 1
                    possibleY = possibleY + 2

                possibleX = crni[i].getX() + 1
                possibleY = crni[i].getY() - 1
                j = 2
                while j > 0:
                    noviCrni = deepcopy(crni)
                    noviBeli = deepcopy(beli)
                    if daLiJePotezMoguc(noviCrni[i], possibleX, possibleY,crni,beli):
                        noviCrni[i].move(possibleX, possibleY)
                        if noviCrni[i].getX() == 8:
                            noviCrni[i].postaniDama()
                        newState = {"beli": noviBeli, "crni": noviCrni, "AI": not stanjeTable["AI"]}
                        possibleStates.append(newState)
                    j = j - 1
                    possibleY = possibleY + 2

                possibleX = crni[i].getX() + 2
                possibleY = crni[i].getY() - 2
                j = 2
                while j > 0:
                    noviCrni = deepcopy(crni)
                    noviBeli = deepcopy(beli)
                    if daLiJePotezMoguc(noviCrni[i], possibleX, possibleY, crni, beli):
                        if noviCrni[i].getX()<possibleX:
                            searchX=1+noviCrni[i].getX()
                        else:
                            searchX=-1+noviCrni[i].getX()

                        if noviCrni[i].getY()<possibleY:
                            searchY=1+noviCrni[i].getY()
                        else:
                            searchY=-1+noviCrni[i].getY()
                        indx=nadjiFiguru(beli,searchX,searchY)
                        noviBeli.pop(indx)

                        noviCrni[i].move(possibleX, possibleY)
                        if noviCrni[i].getX() == 8:
                            noviCrni[i].postaniDama()
                        newState = {"beli": noviBeli, "crni": noviCrni, "AI": not stanjeTable["AI"]}
                        possibleStates.append(newState)
                    j = j - 1
                    possibleY = possibleY + 4

                possibleX = crni[i].getX() - 2
                possibleY = crni[i].getY() - 2
                j = 2
                while j > 0:
                    noviCrni = deepcopy(crni)
                    noviBeli = deepcopy(beli)
                    if daLiJePotezMoguc(noviCrni[i], possibleX, possibleY, crni, beli):
                        if noviCrni[i].getX() < possibleX:
                            searchX = 1 + noviCrni[i].getX()
                        else:
                            searchX = -1 + noviCrni[i].getX()

                        if noviCrni[i].getY() < possibleY:
                            searchY = 1 + noviCrni[i].getY()
                        else:
                            searchY = -1 + noviCrni[i].getY()
                        indx = nadjiFiguru(beli, searchX, searchY)
                        noviBeli.pop(indx)

                        noviCrni[i].move(possibleX, possibleY)
                        if noviCrni[i].getX() == 8:
                            noviCrni[i].postaniDama()
                        newState = {"beli": noviBeli, "crni": noviCrni, "AI": not stanjeTable["AI"]}
                        possibleStates.append(newState)
                    j = j - 1
                    possibleY = possibleY + 4



    return possibleStates
