class Figura:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        self.__tip="obican"

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def getTip(self):
        return self.__tip

    def setX(self,x):
        self.__x=x

    def setY(self,y):
        self.__y=y

    def postaniDama(self):
        self.__tip="dama"

    def move(self,x,y):
        self.__x=x
        self.__y=y

    def daLiJeDama(self):
        if self.__tip=="dama":
            return  True
        return False

