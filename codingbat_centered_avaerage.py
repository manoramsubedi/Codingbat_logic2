"""Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, 
ignore just one copy, and likewise for the largest value. Use int division to produce the final average. 
You may assume that the array is length 3 or more.


centered_average([1, 2, 3, 4, 100]) → 3
centered_average([1, 1, 5, 5, 10, 8, 7]) → 5
centered_average([-10, -4, -2, -4, -2, 0]) → -3
"""
nums = [4, 0, 100]
if len(nums)>=3:
    small = min(nums)
    big = max(nums)

    # count_small = nums.count(small)
    # count_big = nums.count(big)

    #if count_big > 1:
    nums.remove(big)
    #if count_small > 1:
    nums.remove(small)

    print("Avg:",int(sum(nums)/len(nums)))

# print("Small:",small)
# print("Small count:",count_small)
# print("Big:",big)
# print("Big count",count_big)
# print(nums)
