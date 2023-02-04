class summa:

    def __init__(self):
        print("Dastur ishga tushdi")
        self.x = 0
        self.s = 0
        
    def tekshir(self):
        while True:
            b = False
            try:
                self.x = int(self.son())
                b = True
                self.s = self.xisobla()
            except:
                print("sonni qaytadan kirgiz:")
            if b == True:
                print("yig'indi:", self.s)
                break

    def xisobla(self):
        for i in range(self.x + 1):
            i = int(i)
            self.s = self.s + i
        return self.s

    def son(self):
        return input("chegarani kirgiz:")

a = summa()

a.tekshir()
