"""
Return True if the string "cat" and "dog" appear the same number of times in the given string.


cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""

str = "catcat"
cat_count = str.count('cat')
dog_count = str.count('dog')
if cat_count == dog_count:
    print("equal count")
else:
    print("Not equal count")