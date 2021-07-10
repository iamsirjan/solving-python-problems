def clockAngle(h,  m):
    minuteangle = 6 * m
    if m == 60:
        hourangle = 30 * h
    else:
        hourangle = 30 * h + 0.5*m

    angle = hourangle - minuteangle
    print(angle)


hour = int(input("Enter your hour: "))
min = int(input("Enter your min:"))
clockAngle(hour, min)
