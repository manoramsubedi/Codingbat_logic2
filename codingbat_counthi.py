"""
Return the number of times that the string "hi" appears anywhere in the given string.


count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2"""

count=0
m='ABChi hi'
str = m.lower()

for i in range(len(str)-1):
    #print(i,",",i+1)
    if str[i:i+2] == 'hi':
        count+=1
print(count)
