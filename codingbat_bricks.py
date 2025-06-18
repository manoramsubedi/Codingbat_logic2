
def bricks(s, b, goal): 
    lbricks = goal // 5 #2
    
    if lbricks>b:
        lbricks = b
        
    goal = goal - (lbricks*5) #13-10=3
    if goal<=s:
        return True
    return False
        
        



x = bricks(7, 1, 13)
if x:
    print("True")
else:
    print("False")


# 2x1=2
# 4x5=20

# 15+2=17