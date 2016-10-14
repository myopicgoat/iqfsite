lr = lr_aapl
df,loc,scale = t.fit(lr)
fig2.append_trace(Scatter(x=x,y=t.pdf(x,df,loc,scale),showlegend=False),1,1)
#
lr = lr_goog
df,loc,scale = t.fit(lr)
fig2.append_trace(Scatter(x=x,y=t.pdf(x,df,loc,scale),showlegend=False),1,2)
#
iplot(fig2)
