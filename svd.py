import numpy as np
import time

# Define the matrices
matrices = [
    np.array([[2, 1],
              [1, 0]]),
    
    np.array([[2, 1],
              [1, 0],
              [0, 1]]),
    
    np.array([[2, 1, -1],
              [1, 0, 1],
              [1, 1, 1],
              [2, -1, 1]]),
    
    np.array([[1, 1, 0],
              [-1, 0, 1],
              [0, 1, -1],
              [1, 1, -1]]),
    
    np.array([[1, 1, 0],
              [-1, 0, 1],
              [0, 1, -1],
              [1, 1, -1]]),
    
    np.array([[0, 1, 1],
              [0, 1, 0],
              [1, 1, 0],
              [0, 1, 0],
              [1, 0, 1]])
]

# Compute SVD for each matrix
for i, matrix in enumerate(matrices, start=1):
    print(f"\nSVD of matrix {i}:")
    start_time = time.time()
    U, S, Vt = np.linalg.svd(matrix)
    end_time = time.time()
    time_taken = end_time - start_time

    # Print time taken
    print("Time taken: {:.6f} seconds".format(time_taken))

    # Demonstrate correctness
    print("U:")
    print(U)
    print("S (Singular values):")
    print(np.diag(S))
    print("Vt (Transpose of V):")
    print(Vt)
