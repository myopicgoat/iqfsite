def callPriceBS(St,K,tau,r,v):
    d1 = ( (np.log(St/K)) + (r+np.power(v,2)/2)*tau ) / (v*np.sqrt(tau))
    d2 = d1-v*np.sqrt(tau)
    return St*norm.cdf(d1)-K*np.exp(-r*tau)*norm.cdf(d2)
