def A(n,m):
  if n==0:
    return n+1
  elif m==0:
    return A(n-1,1)
  else:
    return A(n-1,A(n,m-1))
