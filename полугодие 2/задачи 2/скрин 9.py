class Product:
    def __init__(self, name, zxc, qua):
        self.name=name
        self.zxc=zxc
        self.qua=qua
    def a_qua(self, summa):
        self.qua+=summa
    def b_qua(self, summa):
        if self.qua-summa>=0:
            self.qua-=summa
        else:
            print(f'недостаточное количество {self.name}')
    def total(self):
        return self.zxc*self.qua
a=Product('Кокс', 67, 69)
b=Product('ьмыщжваоп', 1, 20)
a.a_qua(10)
print(a.qua)
b.b_qua(50)
print(b.qua)
print(a.total())
print(b.total())