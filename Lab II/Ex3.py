from math import sqrt


# class Complex(object):
#     def __init__(self, c, d):
#         self.__real = c
#         self.__imag = d*1j
#
#     def getRealPart(self):
#         return self.__real
#
#     def getImaginaryPart(self):
#         return self.__imag
#
#     def __str__(self):
#         if self.__imag == 0:
#             result = "%.1f+0.00i" % self.__real
#         elif self.__real == 0:
#             if self.__imag >= 0:
#                 result = "0.00+%.1fi" % self.__imag
#             else:
#                 result = "0.00-%.1fi" % (abs(self.__imag))
#         elif self.__imag > 0:
#             result = "%.2f+%.2fi" % (self.__real, self.__imag)
#         else:
#             result = "%.2f-%.2fi" % (self.__real, abs(self.__imag))
#         return result
#
#     def __add__(self, other):
#         return Complex(self.__real + other.c, (self.__imag + other.d))
#
#     def __sub__(self, other):
#         return Complex(self.__real - other.c, (self.__imag - other.d))
#
#     def __mul__(self, other):
#         return Complex((self.__real * other.c) - (self.__imag * other.d), (self.__imag * other.c) +
#                        (self.__real * other.d))
#
#     def __truediv__(self, other):
#         denomi = (other.c ** 2 + other.d ** 2)
#         return Complex(((self.__real * other.c) - (self.__imag * other.d)) / denomi, ((self.__imag * other.c) +
#                                                                                       (self.__real * other.d)) / denomi)
#
#     def __abs__(self):
#         return Complex(sqrt(self.__real ** 2 + self.__imag ** 2))

class Complex:
    def __init__(self, c, d):
        self.__real = c
        self.__imag = d * 1j

    def getRealPart(self):
        return self.__real

    def getImaginaryPart(self):
        return self.__imag

    def __add__(self, other):
        return (self.__real + other.getRealPart()) + (self.__imag + other.getImaginaryPart())

    def __sub__(self, other):
        return (self.__real - other.getRealPart()) + (self.__imag - other.getImaginaryPart())

    def __mul__(self, other):
        return ((self.__real * other.getRealPart() - self.__imag * other.getImaginaryPart()) +
                (self.__imag * other.getRealPart() + self.__real * other.getImaginaryPart()))

    def __truediv__(self, other):
        d = other.getRealPart()**2 + other.getImaginaryPart()**2
        return (((self.__real * other.getRealPart() + self.__imag * other.getImaginaryPart())/d) +
                ((self.__imag * other.getRealPart() - self.__real * other.getImaginaryPart())/d))

    def __abs__(self):
        avp = pow(self.__real, 2) + pow(self.__imag, 2)
        return avp

    def __str__(self):
        if self.__imag == 0:
            return str(self.__real)
        return str(self.__real + self.__imag)
