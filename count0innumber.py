def count(number, count):
    numbers = str(number)
    numberlen = len(numbers)
    for i in range(0, numberlen):

        if numbers[i] == '0':
            count += 1
            i += 1
    print(count)


number = int(12345602120021210)
initcount = 0
count(number, initcount)
