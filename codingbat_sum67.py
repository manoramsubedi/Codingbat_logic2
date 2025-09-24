"""
Return the sum of the numbers in the array, except ignore sections of numbers 
starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). 
Return 0 for no numbers.


sum67([1, 2, 2]) → 5
sum67([1, 2, 2, 6, 99, 99, 7]) → 5
sum67([1, 1, 6, 7, 2]) → 4
sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) → 2
sum67([6, 7, 1, 6, 7, 7]) → 8
"""

nums = [1, 6, 2, 2, 7, 1, 6, 99, 99, 7]
total = 0
ignore = False
for num in nums:
    if num == 6:
        ignore = True
    elif num == 7 and ignore:
        ignore = False
    elif not ignore:
        total += num
print(total)

# while 6 in nums and 7 in nums:
#     ind6 = nums.index(6)
#     ind7 = nums.index(7)
#     if ind6 < ind7:
#         del nums[ind6:ind7+1]
    
# print(nums)
# print(sum(nums))
