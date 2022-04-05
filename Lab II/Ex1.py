class LinearEquation:
    def __init__(self, a=0.0, b=0.0, c=0.0, d=0.0, e=0.0, f=0.0):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getE(self):
        return self.__e

    def getF(self):
        return self.__f

    def isSolvable(self):
        if (self.__a * self.__d) - (self.__b * self.__c) != 0:
            return True

    def getX(self):
        return ((self.__e * self.__d)-(self.__b * self.__f))/((self.__a * self.__d)-(self.__b * self.__c))

    def getY(self):
        return ((self.__a * self.__f)-(self.__e * self.__c))/((self.__a * self.__d)-(self.__b * self.__c))
