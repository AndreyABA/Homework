class student:
    def __init__(self, name, age, zxc=None):
        self.name=name
        self.age=age
        self.zxc=zxc or {}
    def add_predmet(self, predmet, zxc1):
        self.zxc[predmet]=zxc1
    def remove_predmet(self, predmet):
        if predmet in self.zxc:
            del self.zxc[predmet]
        else:
            print(f"Предмета {predmet} нет в списке")
    def avgzxc(self):
        return sum(self.zxc.values()) / len(self.zxc) if self.zxc else 0
andrey=student('Андрей', 69)
andrey.add_predmet('Окружающий мир', 5)
andrey.add_predmet('Сигмология', 5)
andrey.add_predmet('Программирование', 2)
print(andrey.avgzxc())
