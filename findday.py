# suppose we have 1st April 1983 then
# take k =1 , m=2, D=83, c=19
# as march =1 , april =2 ,  ....... janauary 11 , feb 12
# we have formula F = k + [(13*m-1)/5]+ D + [D/4] + [C/4]-2*C


def findDay(date, month, year):
    if month == 'march':
        m = 1
    elif month == 'april':
        m = 2
    elif month == 'may':
        m = 3
    elif month == 'june':
        m = 4
    elif month == 'july':
        m = 5
    elif month == 'august':
        m = 6
    elif month == 'september':
        m = 7
    elif month == 'october':
        m = 8
    elif month == 'november':
        m = 9
    elif month == 'december':
        m = 10
    elif month == 'janauary':
        m = 11
    elif month == 'febrauary':
        m = 12
    else:
        print('enter month correctly')

    k = date
    year = str(year)
    d = int(year[-2:])
    c = int(year[:2])

    f = k + int((13*m-1)/5) + int(d) + int(d/4) + int(c/4) - (2*c)
    print(f)
    f = int(f % 7)
    print(f)
    if f == 0:
        print('sunday')
    elif f == 1:
        print('monday')
    elif f == 2:
        print('tuesday')
    elif f == 3:
        print('wenesday')
    elif f == 4:
        print('thursday')
    elif f == 5:
        print('friday')
    elif f == 6:
        print('saturday')
    else:
        print('sorry!!')


a = int(input('enter day'))
b = input('enter month')
c = int(input('enter year'))
findDay(a, b, c)
