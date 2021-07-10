def addArray(arr, n, sum):
    for i in range(0, n):
        sum += arr[i]
        i += 1

    print(sum)


A = [1, 2, 3]
print('our array is')
print(A)
sum = 0
addArray(A, 3, sum)
