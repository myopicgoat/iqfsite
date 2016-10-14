
# inline function to compute the lagged-log returns for an arbitrary lag
llr = lambda prices, lag: np.log(prices[range(0+lag,len(prices),    lag)] / 
                                 prices[range(0,    len(prices)-lag,lag)])

# compute the log-returns corresponding to ratios over 5 quotes
# play with the lag afterwards to see what changes in the analysis
lag      = 5  
llr_aapl = llr(aapl,lag)
llr_goog = llr(goog,lag)
#
h_aapl = Histogram(x=llr_aapl,name="AAPL", 
                    histnorm = "probability density", nbinsx = 50)
h_goog = Histogram(x=llr_goog,name="GOOG", 
                    histnorm = "probability density", nbinsx = 50)
fig = tools.make_subplots(rows=1,cols=2)

fig.append_trace(h_aapl,1,1)
fig.append_trace(h_goog,1,2)

fig['layout']['xaxis1'].update(range=[-.3,.3])
fig['layout']['yaxis1'].update(range=[0,15])
fig['layout']['xaxis2'].update(range=[-.3,.3])
fig['layout']['yaxis2'].update(range=[0,15])

mu,sigma = norm.fit(llr_aapl)
fig.append_trace(Scatter(x=x,y=norm.pdf(x,mu,sigma),showlegend=False),1,1)
#
mu,sigma = norm.fit(llr_goog)
fig.append_trace(Scatter(x=x,y=norm.pdf(x,mu,sigma),showlegend=False),1,2)

iplot(fig)
