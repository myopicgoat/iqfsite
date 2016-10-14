lr_aapl = np.log(aapl[1:]/aapl[0:-1])
lr_goog = np.log(goog[1:]/goog[0:-1])

data = [
        Scatter(x = aapl_d[1:], y = lr_aapl, name = "AAPL"),
        Scatter(x = aapl_d[1:], y = lr_goog, name = "GOOG")
    ]

layout = Layout(
    xaxis = dict(title = "Trading days [2005-2013]"),
    yaxis = dict(title = "Log-returns"),
    width = 700,
)
fig = dict(data = data, layout = layout)
iplot(fig)