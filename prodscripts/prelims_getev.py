#outcomes:       {HH    HT    TH    TT  }
probs = np.array([1./4, 1./4, 1./4, 1./4])
gains = np.array([10  , 5   , 5   , 0   ])

print("Expected gains: {} GBP".format(np.dot(probs,gains))) 
