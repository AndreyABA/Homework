a=int(input('Введите длину числа '))
def happy(n):
    poln=n // 2
    l=0
    for left_part in range(10**(poln-1), 10**poln):
        for right_part in range(10 ** (poln - 1), 10**poln):
            left_sum=sum(int(digit) for digit in str(left_part))
            right_sum=sum(int(digit) for digit in str(right_part))
            if left_sum==right_sum:
                l+=1
    return l
b=happy(a)
print(f'"счастливых" чисел длины {a} - {b}')
