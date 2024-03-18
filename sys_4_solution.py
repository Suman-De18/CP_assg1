import numpy as np
a=np.array([[4,1,1,0,1],[-1,-3,1,1,0],[2,1,5,-1,-1],[-1,-1,-1,4,0],[0,2,-1,1,4]])
b=np.array([[6],[6],[6],[6],[6]])
x=np.linalg.solve(a,b)
print(x)
print("Solution of the system are :","x1=",x[0],"x2=",x[1],"x3=",x[2],"x4=",x[3],"x5=",x[4])