import numpy as np

class LinearModel:
    def __init__(self, A=np.array([]), B=np.array([]), C=np.array([]), minmax="MAX"):
        self.A = A
        self.B = B
        self.C = C
        self.minmax = minmax
        self.optimized = False  
        self.feasible = True
        self.tableau = np.array([])
        self.basicVariableNo = self.A.shape[0]
        self.solnVarNo = self.C.size
        self.basicVars = np.ones(self.basicVariableNo) * self.basicVariableNo
        self.optimizedValue = 0
        self.optimizedVars = np.zeros(self.basicVariableNo)

    def setA(self, A):
        self.A = A

    def setB(self, B):
        self.B = B

    def setC(self, C):
        self.C = C
        self.basicVariableNo = self.C.size

    def createTableau(self):
        if self.A.size == 0 or self.B.size == 0 or self.C.size == 0:
            print("The constraints are not defined")
            exit()
    
        self.tableau = np.vstack((self.A, -self.C))
        self.tableau = np.hstack((self.tableau, np.identity(self.tableau.shape[0])))
        self.tableau = np.hstack((self.tableau, np.atleast_2d(np.append(self.B, 0)).T))

    def pivotCol(self):
        if not self.optimized:
            self.objRow = self.tableau[-1]
            self.pcol = min(np.where(self.objRow == min(self.objRow))[0])


    def pivotElement(self):
        nonneg = [i for i in range(self.B.size) if self.tableau[i, self.pcol] > 0]
        if nonneg == []:
            self.feasible = False
            print("The solution is not feasible")
        
        else:
            division = [self.tableau[i][-1]/self.tableau[i][self.pcol] for i in nonneg]
            self.prow = nonneg[division.index(min(division))]
            self.pelem = self.tableau[self.prow][self.pcol]

    def simplex(self):
        if self.feasible:
            self.basicVars[self.prow] = self.pcol

            self.tableau[self.prow] /= self.pelem
            for i in range(self.tableau.shape[0]):
                if i != self.prow:
                    self.tableau[i] = self.tableau[i] - self.tableau[self.prow] * self.tableau[i][self.pcol] 

    def checkOptimized(self):
        if self.feasible:
            optcheck = self.tableau[-1][:self.solnVarNo]
            self.optimized = True
            for x in optcheck:
                if x < 0:
                    self.optimized = False

    def optimize(self):
        self.createTableau()
        self.checkOptimized()
        while self.feasible and not self.optimized:
            self.pivotCol()
            self.pivotElement()
            self.simplex()
            self.checkOptimized()

    def optimalSoln(self):
        if self.optimized:
            sol = np.zeros(self.solnVarNo)
            for i in range(self.solnVarNo):
                if i in self.basicVars:
                    sol[i] = self.tableau[np.where(self.basicVars == i)[0], -1]
            return sol
        return "The value is not optimized yet you fool"

    def optimalVal(self):
        if self.optimized:
            return self.tableau[-1, -1]

