
"""
Given two strings, return True if either of the strings appears at the very end of the other string, 
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
"""

a = "xyz"
b = '12xyz'

a = a.lower()
b = b.lower()
print(a.endswith(b) or b.endswith(a))

# if str[-1].lower() == str1[-1].lower():
#     print("True")
# else:
#     print("False")
