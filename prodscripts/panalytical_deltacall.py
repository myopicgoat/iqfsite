
def callDeltaBS(St,K,tau,r,v):
    d1 = ( (np.log(St/K)) + (r+np.power(v,2)/2)*tau ) / (v*np.sqrt(tau))
    return norm.cdf(d1)

def callDeltaNumerical(St,K,tau,r,v): 
    deltaS = St/1000
    Vplus  = callPriceBS(St+deltaS,K,tau,r,v)
    V      = callPriceBS(St,K,tau,r,v)
    return (Vplus-V)/deltaS