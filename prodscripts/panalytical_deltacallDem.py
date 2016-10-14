
dAnalytical = callDeltaBS(60,75,2,0.05,0.1)
dNumerical  = callDeltaNumerical(60,75,2,0.05,0.1)
pctDiff     = np.abs(dAnalytical-dNumerical)/dAnalytical*100

print("Delta (Analytical): ", dAnalytical)
print("Delta (Numerical) : ", dNumerical)
print("Percentage diff   : ", pctDiff)