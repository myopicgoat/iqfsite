
K = 100 # Strike Price
S = np.linspace(90,110,100)
Vcall = np.maximum((S-K),0.)
Vput  = np.maximum((K-S),0.)
Vstraddle = Vcall+Vput
lstraddle = Scatter(x = S, y = Vstraddle, line = dict( width = 4 ),name="Long straddle") 

layout = Layout( 
    xaxis = dict(title = "Underlying asset price at maturity - S_T"),
    yaxis = dict(title = "Payoff at maturity - V_T",tickvals = [ 0.0, 10.0]),
    width = 700
)
fig = dict(data = [lstraddle], layout = layout)
iplot(fig)
