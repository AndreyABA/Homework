import csv
def func(name, name2):
    a=0
    b=0
    with open(name, newline='', encoding="utf-8") as file:
        reader=csv.DictReader(file)
        for row in reader:
            a+=float(row[name2])
            b+=1
    avg=a/b if b!=0 else 0
    print(f"Среднее значение по столбцу '{name2}': {avg}")
func('data2.csv', 'temp')
