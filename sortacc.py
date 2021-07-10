def sortArray(A, n):
    for i in range(0, n-1):
        for j in range(i+1, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
                i += 1
                j += 1


A = [1, 4, 3, 7, 8, 9]
print(A)
sortArray(A, 6)
print("Sorted Arr is ")
print(A)
