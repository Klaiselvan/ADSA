def matrix_chain_multiplication(dims):
    n = len(dims) - 1  # Number of matrices
    # Create a memoization table to store intermediate results
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    # Initialize the memoization table
    for i in range(n):
        m[i][i] = 0

    # Fill the memoization table using a bottom-up approach
    for chain_length in range(2, n + 1):
        for i in range(n - chain_length + 1):
            j = i + chain_length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    # Reconstruct the optimal parenthesization
    def parenthesize(i, j):
        if i == j:
            return f'Matrix {i + 1}'
        else:
            k = s[i][j]
            left = parenthesize(i, k)
            right = parenthesize(k + 1, j)
            return f'({left} × {right})'

    optimal_parenthesization = parenthesize(0, n - 1)
    min_scalar_multiplications = m[0][n - 1]

    return optimal_parenthesization, min_scalar_multiplications

# Input: List of matrices with their dimensions
matrices = [(2, 3), (3, 4), (4, 2)]

# Find the optimal parenthesization and minimum scalar multiplications
parenthesization, min_mults = matrix_chain_multiplication(matrices)

print("Optimal Parenthesization:", parenthesization)
print("Minimum Scalar Multiplications:", min_mults)
