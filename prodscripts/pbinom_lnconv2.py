
from numpy import trapz

logreturns = np.log(returns)

# the theory gives us the mean and variance
# at the limit when N goes to infinity
# the last line is to "normalize" so that the curves and
# the points are on the same scale 
# (you can safely ignore all this)
th_mean = N*(p*np.log(u)+(1-p)*np.log(d))
th_var  = N*p*(1-p)*np.log(d/u)**2
pr_norm  = probas / abs(trapz(logreturns,probas))

# show the possible log-returns with their weights
s  = Scatter(x=logreturns,y=pr_norm, mode='markers',name="Log returns")
# show the normal distribution with the theoretical mean and variance
# computed above
xx = np.linspace(np.min(logreturns),np.max(logreturns),100)
yy = norm.pdf(xx,th_mean,np.sqrt(th_var))
s2 = Scatter(x=xx,y=yy,name="Normal fit")
#
layout = Layout(
    xaxis = dict(title = "Log-Returns"),
    yaxis = dict(title = "Probability"),
    width = 700,
)
fig = dict(data=[s,s2],layout=layout)
iplot(fig)