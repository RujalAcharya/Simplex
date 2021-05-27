# Simplex

This is a simple implementation of the simplex method, which is a simple method for solving linear programming problems (LPPs).

## Installing the requirements
The only requirement for this progrram is numpy which can be installed as

```
pip install -r requirements.txt
```

## Using the code
The LPP is divided into three numpy arrays (say A, B, C).

Consider the LPP as \
Maximize F = c<sub>1</sub>x<sub>1</sub>+c<sub>2</sub>x<sub>2</sub> \
Subject to constraints \
a<sub>11</sub>x<sub>1</sub>+a<sub>12</sub>x<sub>2</sub>&le;b<sub>1</sub> \
a<sub>21</sub>x<sub>1</sub>+a<sub>22</sub>x<sub>2</sub>&le;b<sub>2</sub> \
x<sub>1</sub>,x<sub>2</sub>&ge;0

Then we define 3 numpy arrays A, B, C as:
```py
A = np.array([[a11, a12]
            [a21, a22]])
B = np.array([b1, b2])
C = np.array([c1, c2])
```

Now we can use the ``LinearModel`` class to create the simplex tableau and then find the optimal solution.

```py
lm = LinearModel(A, B, C)
```
**OR**
```py
lm = LinearModel()
lm.setA(A)
lm.setB(B)
lm.setC(C)
```

Now we can optimize the solution using
```py
lm.optimize()
```
Now, we can look at the optimized value of {x<sub>1</sub>,x<sub>2</sub>, ...} as a numpy array is returned by ``lm.optimizedSoln()`` method. \
Similarly, we can look at the optimized value of F using ``lm.optimizedVal()`` method.

You can also look at the [example program](example.py) or [example notebook](examples.ipynb) to see how it is applied. 

**Note:** Currently only maximization problems can be solved and minimization problems will soon be implemented as well. Further preetifying and visualization of simplex tableau is also planned to be implemented. \
<sub>Feel free to review my code and roast me. I am just a dumbass.</sub>