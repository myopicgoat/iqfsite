P     = np.linspace(11.,13.,100)
Psell = np.linspace(12.3,13.,50)
Pbuy  = np.linspace(11.,12.3,50)

a1 = lambda P: 7./(P-6.)
a2 = lambda P: -3./(P-15.)

# show P=12.3
a0 = np.linspace(.7,1.5,100) 
P0 = 12.3+a0*0.

p0 = Scatter(x=P0,y=a0,name="AF price")
# regions
r1 = Scatter(x=Psell,y=a1(Psell),showlegend=False)
r2 = Scatter(x=Psell,y=a2(Psell),fill="tonexty",showlegend=False)
r3 = Scatter(x=Pbuy,y=a2(Pbuy),showlegend=False)
r4 = Scatter(x=Pbuy,y=a1(Pbuy),fill="tonexty",showlegend=False)
# boundary curves
p1 = Scatter(x=P,y=a1(P),name="7/(P-6)")
p2 = Scatter(x=P,y=a2(P),name="3/(15-P)")
data = [p0,r1,r2,r3,r4,p1,p2]

layout = Layout(
            xaxis = dict(title = "Price of game 2"),
            yaxis = dict(title = "alpha"),
            width=700
            )
fig = dict(data=data,layout=layout)

iplot(fig)
