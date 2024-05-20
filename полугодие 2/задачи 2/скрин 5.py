class biblioteka:
    def __init__(self):
        self.spisok=[]
    def add_kniga(self, b):
        self.spisok.append(b)
        print(f"книга '{b}' добавлена в библиотеку")
    def remove_kniga(self, b):
        if b in self.spisok:
            self.spisok.remove(b)
            print(f"книга '{b}' удалена из библиотеки")
        else:
            print(f"книги '{b}' нет в библиотеке")
    def find_kniga(self, b):
        if b in self.spisok:
            print(f"книга '{b}' найдена в библиотеке")
        else:
            print(f"книга '{b}' не найдена в библиотеке")
c=biblioteka()
c.add_kniga('Преступление и наказание')
c.add_kniga('Мастер и Маргарита')
c.find_kniga('1984')
