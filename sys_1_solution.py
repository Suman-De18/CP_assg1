import numpy as np
a=np.array([[3,-1,1],[3,6,2],[3,3,7]])
b=np.array([[1],[0],[4]])
x=np.linalg.solve(a,b)
print(x)
print("Solutions of system are:", "x1=",x[0],"x2=",x[1],"x3=",x[2])
