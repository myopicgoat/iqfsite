
lags     = np.array([1,3,5,7,10,15,20])
sig_aapl = np.zeros(len(lags))
mu_aapl  = np.zeros(len(lags))
sig_goog = np.zeros(len(lags))
mu_goog  = np.zeros(len(lags))
i        = 0
for lag in lags:
    mu_aapl[i],sig_aapl[i] = norm.fit(llr(aapl,lag))
    mu_goog[i],sig_goog[i] = norm.fit(llr(goog,lag))
    i+=1
## display mean evolution

data = [
        Scatter(x = lags, y = mu_aapl, name = "AAPL"),
        Scatter(x = lags, y = mu_goog, name = "GOOG")  
    ]
layout = Layout(
    xaxis = dict(title = "Log return lag [days]"),
    yaxis = dict(title = "Fitted means"),
    width = 700,
)
fig = dict(data = data, layout = layout)
iplot(fig)
## display variance evolution

data = [
        Scatter(x = lags, y = sig_aapl**2, name = "AAPL"),
        Scatter(x = lags, y = sig_goog**2, name = "GOOG")  
    ]
layout = Layout(
    xaxis = dict(title = "Log return lag [days]"),
    yaxis = dict(title = "Fitted variance"),
    width = 700,
)
fig = dict(data = data, layout = layout)
iplot(fig)
