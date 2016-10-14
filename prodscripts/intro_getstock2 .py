l1 = Scatter(x = aapl_d, y = aapl, name = "AAPL")
l2 = Scatter(x = goog_d, y = goog, name = "GOOG")
data = [l1,l2]

layout = Layout(
    xaxis = dict(title = "Trading days [2005-2013]"),
    yaxis = dict(title = "Prices"),
    width = 700,
)
fig = dict(data = data, layout = layout)
iplot(fig)