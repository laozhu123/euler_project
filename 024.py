from math import factorial
def perm(n, s):
   if len(s)==1:
       return s
   q, r = divmod(n, factorial(len(s)-1))
   return s[q] + perm(r, s[:q] + s[q+1:])

L = 1000000
print ("Project Euler 24 Solution = ", perm(L-1, '0123456789'))