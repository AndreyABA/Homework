def func():
    with open("file.txt", "w", encoding="utf-8") as file:
        file.write('первая строка\n')
        file.write('вторая строка\n')
        file.write('третья строка')
func()
def func2(a):
    with open(a, "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
func2("file.txt")
