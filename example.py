from linearmodel import LinearModel 
import numpy as np

A = np.array([[2, 1], [1, 1], [1, 2]])
B = np.array([10, 7, 12])
C = np.array([30, 40])

lm = LinearModel(A, B, C)
lm.optimize()

if __name__=="__main__":
    print(lm.tableau)
    print(lm.optimizedSoln())
    print(lm.optimizedVal())