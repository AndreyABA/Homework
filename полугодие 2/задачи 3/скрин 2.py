import csv
def func():
    with open("data.csv", "w", newline='', encoding="utf-8") as file:
        writer=csv.writer(file)
        writer.writerow(['имя', 'фамилия', 'возраст'])
        writer.writerow(['Андрей', 'Абакумов', '14'])
        writer.writerow(['Иосиф', 'Сталин', 'умер'])
func()
def func2(a):
    with open(a, newline='', encoding="utf-8") as file:
        reader =csv.reader(file)
        for row in reader:
            print(" ".join(row))
func2("data.csv")
