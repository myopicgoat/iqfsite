h_aapl = Histogram(x=lr_aapl,name="AAPL", 
                    histnorm = "probability density", nbinsx = 70)
h_goog = Histogram(x=lr_goog,name="GOOG", 
                    histnorm = "probability density", nbinsx = 70)

fig = tools.make_subplots(rows=1,cols=2)

fig.append_trace(h_aapl,1,1)
fig.append_trace(h_goog,1,2)

fig['layout']['xaxis1'].update(range=[-.15,.15])
fig['layout']['yaxis1'].update(range=[0,30])
fig['layout']['xaxis2'].update(range=[-.15,.15])
fig['layout']['yaxis2'].update(range=[0,30])

iplot(fig)
