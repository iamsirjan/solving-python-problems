def square(n):
    for i in range(1, n):
        if i*i < n:
            print(i)
            i += 1


n = 9
square(n)
