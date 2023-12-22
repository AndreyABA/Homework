def search_substr(subst, st):
    subst_a=subst.lower()
    st_a=st.lower()
    if subst_a in st_a:
        return 'есть контакт'
    else:
        return 'мимо'
stroka1='стр'
stroka2='бессмысленная строка'
print(search_substr(stroka1, stroka2))