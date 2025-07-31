"""
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. 
Return -1 if it can't be done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2 

make_chocolate(60, 100, 550) → 50

make_chocolate(9, 3, 18) → 3
"""

#def make_chocolate(small, big, goal): 
#     big_req = goal//5 
   
#     if big_req > big: 
#         big_val = big*5 
#     else: 
#         big_val = big_req*5

#     if big_val == goal:
#         return 0

#     elif big_val < goal: 
#         small_req = goal - big_val 
#         if small_req <= small:
#             return small_req 
#         else: return -1
#     else:
#         return -1

# x=make_chocolate(6, 1, 11)
# print(x)

def make_chocolate(small, big, goal):
    big_used = min(goal // 5, big)  # ues as many big bars as possible
    remaining = goal - (big_used * 5)

    if remaining <= small:
        return remaining  #number of small bars needed
    else:
        return -1


