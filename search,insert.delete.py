def insert(A, i, v):
    A.insert(i, v)
    print('value inserted sucessfully')
    print(A)


def delete(A, n, v):
    for i in range(0, n):
        if A[i] == v:
            A.remove(v)
            print('deleted successfully')
            print(A)


def search(A, n, v):
    for i in range(0, n):
        if A[i] == v:
            print('search found')
        else:
            print('no search found')


A = [1, 2, 3, 4, 5]
# value = int(input("enter value you want to insert"))
# index = int(input("enter index where you want to insert value"))
# insert(A, index, value)

# value = int(input("enter value you want to delete"))
# # index = int(input("enter index where you want to insert value"))
# delete(A, 5, value)


value = int(input('enter number to search'))
search(A, 5, value)
