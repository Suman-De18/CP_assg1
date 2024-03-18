import numpy as np
a=np.array([[10,5,0,0],[5,10,-4,0],[0,-4,8,-1],[0,0,-1,5]])
b=np.array([[6],[25],[-11],[-11]])
x=np.linalg.solve(a,b)
print(x)
print("Solution of the system are :","x1=",x[0],"x2=",x[1],"x3=",x[2],"x4=",x[3])