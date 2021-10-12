import math

def MiniMax(cvor):
    for child in cvor.children:
        MiniMax(child)
    if not cvor.is_leaf():
        if cvor.data["AI"]:
            max=-1*math.inf
            for child in cvor.children:
                if child.score>max:
                    max=child.score
            cvor.score=max
        else:
            min=math.inf
            for child in cvor.children:
                if child.score<min:
                    min=child.score
            cvor.score=min

def heuristika(tabla):
    beli=tabla["beli"]
    crni=tabla["crni"]

    if len(beli)==0:
        return -1*math.inf
    if len(crni)==0:
        return  math.inf
    beliScore=0
    for figura in beli:
        if figura.daLiJeDama():
            beliScore=beliScore+5
        elif figura.getY()==1 or figura.getY()==8:
            beliScore=beliScore+2
        else:
            beliScore=beliScore+1
    crniScore=0
    for figura in crni:
        if figura.daLiJeDama():
            crniScore=crniScore+5
        elif figura.getY()==1 or figura.getY()==8:
            crniScore=crniScore+1.5
        else:
            crniScore=crniScore+1

    return beliScore-crniScore


def izracunajZaListove(node):
    if node.is_leaf():
        node.score=heuristika(node.data)
    else:
        for child in node.children:
            izracunajZaListove(child)
