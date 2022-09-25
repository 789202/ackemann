def A(a,b,c):
  if a==0 and b==a:
    return c+1
  else:
    if b==0:
      return A(a-1,c,c)
    else:
      if c==0:
        return A(a,b-1,1)
      else:
        return A(a,b-1,A(a,b,c-1))
def f(n):
  if n==0:
    return 1
  else:
    return A(f(n-1),f(n-1),f(n-1))
print(f(f(99)))
