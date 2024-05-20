class Soda:
    def __init__(self, a=None):
        self.a=a
    def showmydrink(self):
        if self.a:
            print(f"газировка и {self.a}")
        else:
            print("обычная газировка")
soda=Soda('моча')
soda.showmydrink()
