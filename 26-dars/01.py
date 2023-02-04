import os

class Xisoblash:

    def __init__(self):
        print("Dastur ishga tushdi\n")
        self.son = 0

    def boshla(self):
        self.tekshir()

    def tekshir(self):
        try:
            self.son = int(self.son_ol())
            self.son_xisobla()
        except:
            print('siz son kiritmadingiz')
    
    def son_xisobla(self):
        print(bin(self.son))

    def son_ol(self):
        return input("10 likda son kiriting: \n")


a = Xisoblash()
a.boshla()
    
