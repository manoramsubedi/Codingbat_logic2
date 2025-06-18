# (1,2,4) -> 7
# (2,3,3) -> 5
# (2,2,2) -> 0 

a,b,c = 9,9,9
# sum=0
# l = [a,b,c]
# new=[]
# for i in l:
#     if i in new:
#         new.remove(i)
#     else:
#         new.append(i)

# if len(set(l))==1 :
#     print(0)
# else:
#     for i in new:
#         sum += i
#     print(sum)



sum = 0 
if a!=b and a!=c:
    sum += a
if b!=a and b!=c:
    sum += b
if c!=a and c!=b:
    sum += c

print(sum)

