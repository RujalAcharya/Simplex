from linearmodel import LinearModel 
import numpy as np

A = np.array([[-2, 1], [-1, 1], [0, 1]])
B = np.array([2, 5, 6])
C = np.array([2, 3])

lm = LinearModel(A, B, C)
lm.optimize()

# if __name__=="__main__":
#     print(lm.tableau)
#     print(lm.optimalSoln())
#     print(lm.optimalVal())