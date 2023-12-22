def top3(st):
    st=st.replace(" ", "")
    a={}
    for i in st:
        if i in a:
            a[i]+=1
        else:
            a[i]=1
    b=sorted(a.items(), key=lambda x: x[1], reverse=True)[:3]
    c=", ".join(f"{i} : {count} раз(а)" for i, count in b)
    return c
st='На сердце боль в душе тоска второго нет нигде носка'
print(top3(st))