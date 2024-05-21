import csv
def func(names, b):
    a=[]
    zxc=set()
    for i in names:
        with open(i, newline='', encoding="utf-8") as file:
            reader=csv.DictReader(file)
            zxc.update(reader.fieldnames)
            for row in reader:
                a.append(row)
    zxc=list(zxc)
    with open(b, "w", newline='', encoding="utf-8") as file:
        writer=csv.DictWriter(file, fieldnames=zxc)
        writer.writeheader()
        for row in a:
            writer.writerow(row)
func(['data1.csv', 'data3.csv', 'data4.csv'], 'combined_data.csv')
