# note: there are N+1 final nodes when considering N steps
nPaths = lambda N: [comb(N,k) for k in range(0,N+1)]
print(nPaths(4))
