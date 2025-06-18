
# lucky_sum(1, 2, 3) → 6
# lucky_sum(1, 2, 13) → 3
# lucky_sum(1, 13, 3) → 1

def lucky_sum(a,b,c):
    if a==13:
        print(0)
    elif b==13:
        print(a)
    elif c==13:
        print(a+b)
    else:
        print(a+b+c)
    

lucky_sum(1,2,13)