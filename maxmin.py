def getMin(arr, n):
    res = arr[0]
    for i in range(1, n):
        res = min(res, arr[i])
    return res


def getMax(arr, n):
    res = arr[0]
    for i in range(1, n):
        res = max(res, arr[i])
    return res


arr = [1000, 12, 14, 16, 19, 20, 1, 10]
n = len(arr)
print("min element is :", getMin(arr, n))
print("max element is :", getMax(arr, n))
