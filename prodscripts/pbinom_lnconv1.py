endProbas  = lambda p,N:   [comb(N,k)*(p**k)*(1-p)**(N-k) for k in range(0,N+1)]
endReturns = lambda u,d,N: [(u**k)*(d)**(N-k) for k in range(0,N+1)]
# enter some arbitrary values
p = 0.6  # probability of going up
u = 1.03 # multiplicative "up factor"
d = 0.99 # multiplicative "down factor"

# number of steps (play with this number)
N = 100
returns = endReturns(u,d,N)
probas  = endProbas(p,N)
# display pdf
s = Scatter(x=returns,y=probas, mode='markers')
layout = Layout(
    xaxis = dict(title = "Returns"),
    yaxis = dict(title = "Probability"),
    width = 700,
)
fig = dict(data=[s],layout=layout)
iplot(fig)
