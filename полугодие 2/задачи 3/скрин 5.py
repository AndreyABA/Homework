import xml.etree.ElementTree as et
def create():
    data=et.Element('магазин')
    item1=et.SubElement(data, 'товар')
    item1.set('категория', 'комплектующие')
    et.SubElement(item1, 'название').text = 'rtx 5090'
    et.SubElement(item1, 'цена').text = '180000'
    item2=et.SubElement(data, 'товар')
    item2.set('категория', 'книги')
    et.SubElement(item2, 'название').text = 'Мастер и Маргарита'
    et.SubElement(item2, 'цена').text = '500'
    tree=et.ElementTree(data)
    tree.write('table.xml')
create()
import xml.etree.ElementTree as et
def func(zxc):
    tree=et.parse(zxc)
    root=tree.getroot()
    items=[]
    for item in root.findall('товар'):
        name=item.find('название').text
        price=float(item.find('цена').text)
        category=item.get('категория')
        items.append({'название': name, 'цена': price, 'категория': category})
    items.sort(key=lambda x: x['цена'])
    summa=sum(item['цена'] for item in items)
    print('цены по возрастанию: ')
    for item in items:
        print(f"{item['название']} ({item['категория']}): {item['цена']}")
    print(f"\nОбщая стоимость товаров: {summa}")
func('table.xml')
