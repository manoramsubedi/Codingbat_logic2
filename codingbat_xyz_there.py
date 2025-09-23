
"""
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.


xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
xyz_there('abc.xxyz') → True
"""

st = "abc.xxyz"
if 'xyz' in st:
    if '.xyz' in st:
        print("False")
    print("True")
else:
    print("False")

# if '.xyz' in st:
#     print("False")
#     #break
# elif 'xyz' in st:
#     print("True")
# else:
#     print("False")

# for i in range(len(st)):
#     if st[i] == '.':
#         print("False")
#         break
#     elif 'xyz' in st:
#         print("True")
#     else:
#         print("False")
    #st[i:i+3] == 'xyz':
