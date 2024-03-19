import numpy as np
A=np.array([[5,-2],[-2,8]])
Q, R = np.linalg.qr(A)

print("Q matrix:")
print(Q)
print("\nR matrix:")
print(R)

# eigenvalues after one iteration
A_1=np.dot((np.transpose(Q)),np.dot(A,Q))
eig_val=np.diag(A_1)
print("eigenvalues after 1st step:",eig_val)

# eigenvalues using np.linalg.eigvals
print("actual eigenvalues are:", np.linalg.eigvals(A))

# iterations for better results
for i in range(5):
    Q, R = np.linalg.qr(A)
    A=np.dot(R,Q)
print("eigenvalues after 5 iterations:",np.diag(A))