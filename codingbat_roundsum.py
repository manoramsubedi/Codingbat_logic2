
# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10

#def round_sum(a,b,c):
# num=14
# x=num%10 # 4
# #print(13%10)
# if x>=5:
#     rem = 10-x
#     num = num+rem
# else:
#     num -= x
# print(num)

def round_num(num):
    x=num%10
    if x>=5:
        rem=10-x
        num += rem
    else:
        num -= x
    return num


def round_sum(a,b,c):
    l=[]
    for num in [a,b,c]:
        l.append(round_num(num))
    print(sum(l))

round_sum(20,30,40)