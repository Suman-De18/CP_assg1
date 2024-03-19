import numpy as np
A= np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
eig_val=np.linalg.eigvals(A)
print("Actual eigenvalues are:",eig_val)
x=np.array([[1],[1],[1]])
y=np.array([[1],[0],[0]])
count=0
for i in range(100):
    x=np.dot(A,x)
    count+=1
    lamda=(np.dot(np.transpose(np.dot(A,x)),y))/(np.dot(np.transpose(x),y))
    if abs(np.max(eig_val)-lamda)<0.01:
        break
print("eigenvalues obtained by power method:",lamda)
print("eigenvector corresponding to lamda:",x)
print("number of iterations to get 0.01 tolerance:",count)
