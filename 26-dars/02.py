class yigindi:

    summa = 0
    def __init__(self, x=0, y=0):
        print("Dastur ishga tushdi")
        self.x = x
        self.y = y

    def summa(self):
        return print("yig'indi:", self.tekshir())
    
    def tekshir(self):
        while True:
            b = False
            try:
                self.x = float(self.bir())
                self.y = float(self.ikki())
                b = True
            except:
                print("sonlarni qaytadan kirit:")

            if b == True:
                summa = float(self.x + self.y)
                break

        return summa

    def bir(self):
        return input("birinchi sonni kirit:")

    def ikki(self):
        return input("ikkinchi sonni kirit:")
            

a = yigindi()
a.summa()
