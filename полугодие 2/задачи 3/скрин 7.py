def func(name):
    with open(name, "r", encoding="utf-8") as file:
        text=file.read()
    slova=text.split()
    zxc=len(slova)
    sentences=text.count('.')+text.count('?')+text.count('!')
    avg=sum(len(word) for word in slova)/zxc if zxc!=0 else 0
    print(f"Количество слов: {zxc}")
    print(f"Количество предложений: {sentences}")
    print(f"Средняя длина слова: {avg:.2f}")
func("text1.txt")
