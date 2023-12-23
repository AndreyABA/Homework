def shortener(st):
    while '(' in st or ')' in st:
        a=st.rfind('(')
        b=st.find(')', a)
        st=st.replace(st[a:b + 1], '')
    return st
print(shortener('Какая-то (скобка) фраза ((скобка)) со скобками (скобка)'))