def no_teen_sum(a, b, c):
  total=0
  l = [a,b,c]
  for i in l:
    total += fix_teen(i)
  print(total)
      
def fix_teen(n):
  if 13 <= n <= 19:
    if n == 15 or n == 16:
      return n
    return 0
  return n
  
no_teen_sum(2,13,1)
