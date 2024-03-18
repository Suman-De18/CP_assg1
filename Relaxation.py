import numpy as np
x_true=np.array([[7.859713071],[0.422926408],[-0.073592239],[-0.540643016],[0.010626163]])
A=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
B=np.array([[1],[2],[3],[4],[5]])
D=np.array([[0.2,0,0,0,0],[0,4,0,0,0],[0,0,60,0,0],[0,0,0,8,0],[0,0,0,0,700]])
L=np.tril(D-A)
U=np.triu(D-A)
x=np.array([[0],[0],[0],[0],[0]])
w=1.25
T=np.dot(np.linalg.inv(D-w*L),((1-w)*D + w*U))
C=np.dot(np.linalg.inv(D-w*L),w*B)
count=0
for i in range(100):
    x=np.add(np.dot(T,x),C)
    count+=1
    if abs(x[0]-x_true[0])<0.01 and abs(x[1]-x_true[1])<0.01 and abs(x[2]-x_true[2])<0.01 and abs(x[3]-x_true[3])<0.01 and abs(x[4]-x_true[4])<0.01:
        break
print("approximate solution with tolerance 0.01 are:",x)
print("number of iterations:",count)