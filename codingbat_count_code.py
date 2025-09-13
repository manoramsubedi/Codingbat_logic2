"""
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.


count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""

str = "cozexxcole"
l = []
for i in range(len(str)):
    x = str[i:i+4]
    for i in range(len(x)-3):
        if x[i]=='c' and x[i+1]=='o' and x[i+3]=='e':
            l.append(x)
print(len(l))