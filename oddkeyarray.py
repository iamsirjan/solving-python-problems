def alternateArray(A, n):
    for i in range(0, n):
        if i % 2 == 0:
            print(A[i], end=' ')


A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
alternateArray(A, 9)
