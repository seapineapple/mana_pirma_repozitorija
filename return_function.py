def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

skaitlis1 = int(input('Ievadi pirmo skaitli: '))
skaitlis2 = int(input('Ievadi otro skaitli: '))
liels = maximum(skaitlis1, skaitlis2)
print(maximum(skaitlis1, skaitlis2))