import numpy as np
a=np.array([[10,-1,0],[-1,10,-2],[0,-2,10]])
b=np.array([[9],[7],[6]])
x=np.linalg.solve(a,b)
print(x)
print("Solution of the system are:","x1=",x[0],"x2=",x[1],"x3=",x[2])