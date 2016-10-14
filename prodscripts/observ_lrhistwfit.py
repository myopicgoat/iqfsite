x    = np.linspace(-.15,.15,500)

fig2 = fig # re-use the previous histogram

lr = lr_aapl
mu,sigma = norm.fit(lr)
fig2.append_trace(Scatter(x=x,y=norm.pdf(x,mu,sigma),showlegend=False),1,1)

lr = lr_goog
mu,sigma = norm.fit(lr)
fig2.append_trace(Scatter(x=x,y=norm.pdf(x,mu,sigma),showlegend=False),1,2)

iplot(fig2)
