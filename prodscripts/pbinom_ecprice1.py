
# EUROPEAN CALL

S0 = 100
K  = 99
u  = 1.02
d  = 0.99
# Go forward in the tree for two steps:
S_step1 = S0*np.array([d,u])
S_step2 = S0*np.array([d**2,u*d,u**2])

# Compute risk-neutral probability (r=0)
p_star = (1-d)/(u-d)

# Go backward in the tree with a call
C_step2 = np.array([max(S_step2[i]-K,0.) for i in range(0,3)])
C_step1 = np.array([ p_star*C_step2[1] + (1-p_star)*C_step2[0], 
                     p_star*C_step2[2] + (1-p_star)*C_step2[1]])
C_step0 = p_star*C_step1[1]  + (1-p_star)*C_step1[0]

for step in ("Forward", S0, S_step1, S_step2,
             "Backward",C_step2, C_step1, C_step0):
    print(step)
