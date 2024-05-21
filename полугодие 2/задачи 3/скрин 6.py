import os
import csv
def func(directory):
    zxc={
        'сумм возраст': 0,
        'количество': 0,
        'количество мест': {}}
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            with open(os.path.join(directory, filename), newline='', encoding="utf-8") as file:
                reader=csv.DictReader(file)
                for row in reader:
                    age=int(row.get('вощраст', 0))
                    location=row.get('местоположение', 'неизвестно')
                    zxc['сумм возраст']+=age
                    zxc['количество']+=1
                    if location not in zxc['количество мест']:
                        zxc['количество мест'][location]=0
                    zxc['количество мест'][location]+1
    avg=zxc["total_age"] / zxc["count"] if zxc["count"]!=0 else 0
    print(f"средний возраст: {avg}")
    print('сортировка по местоположению ')
    for location, count in zxc['количество мест'].items():
        print(f"{location}: {count}")
func("data")
