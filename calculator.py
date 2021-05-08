import math

toCalculate = input('What do you want to calculator: > ')

if '+' in toCalculate:  # #+#
    sum = 0
    lstToCalculate = toCalculate.split('+')
    for num in lstToCalculate:
        sum += float(num)
    print(sum)

if '-' in toCalculate:  # #-#
    lstToCalculate = toCalculate.split('-')
    minus = float(lstToCalculate[0])
    for num in range(1, len(lstToCalculate)):
        minus -= float(lstToCalculate[num])
    print(minus)

if '^' in toCalculate:  # when doing multiple exponents: this is how it is calculating: (100^2)^3
    lstToCalculate = toCalculate.split('^')
    exp = float(lstToCalculate[0])
    for num in range(1, len(lstToCalculate)):
        exp **= float(lstToCalculate[num])
    print(exp)

if '*' in toCalculate:
    lstToCalculate = toCalculate.split('*')
    multi = float(lstToCalculate[0])
    for num in range(1, len(lstToCalculate)):
        multi *= float(lstToCalculate[num])
    print(multi)

if '/' in toCalculate:  # calculate multiple divisions like so: ((1/2)/3)/4
    lstToCalculate = toCalculate.split('/')
    divide = float(lstToCalculate[0])
    n = 1
    error = False
    while n != len(lstToCalculate) and not error:
        if int(lstToCalculate[n]) != 0:
            divide /= float(lstToCalculate[n])
            n += 1
        else:  # cannot divide by 0
            error = True
    if error:
        print("You cannot divide by zero.")
    else:
        print('{:.4f}'.format(divide))

if 'ln' in toCalculate:  # natural logarithm; ln(x); don't worry about ln(ln()); ['', '#']
    lstToCalculate = toCalculate.split('ln')
    if float(lstToCalculate[1]) != 0:
        print('{:.4f}'.format(math.log(float(lstToCalculate[1]))))
    else:
        print("You cannot get the natural log of zero.")

if 'sin' in toCalculate:  # sin(x); don't worry about sin(sin(x)); ['', '#']
    lstToCalculate = toCalculate.split('sin')
    print('{:.4f}'.format(math.sin(float(lstToCalculate[1]))))
