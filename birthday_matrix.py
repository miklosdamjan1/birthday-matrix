# Asks for the matrix.
maxdet = 0
mindet = 0
a = 0
wholedate = x = input("When is your birthday?(format: YYYYMMDD)")
original = int(x)
# Asks how many years to calculate.
duration = input("How many years after your birth do you want to calculate?")
x1, x2, x3, x4, x5, x6, x7, x8 = [int(i) for i in str(x)]
# assigning each number to two matrix values
x11 = x31 = x1
x12 = x32 = x2
x13 = x33 = x3
x14 = x34 = x4
x21 = x41 = x5
x22 = x42 = x6
x23 = x43 = x7
x24 = x44 = x8
# calculating the determinant normally without functions
det = x11 * (x22 * (x33 * x44 - x34 * x43) - x23 * (x32 * x44 - x34 * x42) + x24 * (x32 * x43 - x33 * x42)) \
      - x12 * (x21 * (x33 * x44 - x34 * x43) - x23 * (x31 * x44 - x34 * x41) + x24 * (x31 * x43 - x33 * x41)) \
      + x13 * (x21 * (x32 * x44 - x34 * x42) - x22 * (x31 * x44 - x34 * x41) + x24 * (x31 * x42 - x41 * x32)) \
      - x14 * (x21 * (x32 * x43 - x33 * x42) - x22 * (x31 * x43 - x33 * x41) + x23 * (x31 * x42 - x32 * x41))
# min-max determinant of the next 100 years
while True:
    #    if a == 100000:
    #        break
    if int(wholedate) >= original + int(duration) * 10000:
        break

    else:
        if x32 == x33 == x34 == 9 and x41 == 1 and x42 == 2 and x43 == 3 and x44 == 1:
            x31 = x31 + 1
            x32 = x33 = x34 = x44 = x41 = x43 = 0
            x42 = 1
        if x33 == x34 == 9 and x41 == 1 and x42 == 2 and x43 == 3 and x44 == 1:
            x32 = x32 + 1
            x33 = x34 = x41 = x43 = x44 = 0
            x42 = 1
        if x34 == 9 and x41 == 1 and x42 == 2 and x43 == 3 and x44 == 1:
            x33 = x33 + 1
            x34 = x41 = x44 = x43 = 0
            x42 = 1
        if x41 == 1 and x42 == 2 and x43 == 3 and x44 == 1:
            x34 = x34 + 1
            x41 = x43 = x44 = 0
            x42 = 1
        if x42 == 9 and x43 == 3 and x44 == 0:
            x41 = 1
            x42 = x43 = x44 = 0
        if ((x41 == 1 and (x42 == 2 or x42 == 0)) or (
                x41 == 0 and (x42 == 1 or x42 == 3 or x42 == 5 or x42 == 7 or x42 == 8))) and x43 == 3 and x44 == 1:
            x42 = x42 + 1
            x43 = 0
            x44 = 0
        if (x41 == x42 == 1) and x43 == 3 and x44 == 0:
            x42 = x42 + 1
            x43 = 0
            x44 = 0
        if (x41 == 0 and (x42 == 4 or x42 == 6)) and x43 == 3 and x44 == 0:
            x42 = x42 + 1
            x43 = 0
            x44 = 0
        if ((x31 * 1000 + x32 * 100 + x33 * 10 + x34) % 4 == 1 or (
                x31 * 1000 + x32 * 100 + x33 * 10 + x34) % 4 == 2 or (
                    x31 * 1000 + x32 * 100 + x33 * 10 + x34) % 4 == 3) and x41 == 0 and x42 == x43 == 2 and x44 == 8:
            x42 = x42 + 1
            x43 = 0
            x44 = 0
        if x41 == 0 and x42 == x43 == 2 and x44 == 9:
            x42 = x42 + 1
            x43 = 0
            x44 = 0
        x44 = x44 + 1
        if x44 == 10:
            x43 = x43 + 1
            x44 = 0

        #        a = a + 1
        det = x11 * (x22 * (x33 * x44 - x34 * x43) - x23 * (x32 * x44 - x34 * x42) + x24 * (x32 * x43 - x33 * x42)) \
              - x12 * (x21 * (x33 * x44 - x34 * x43) - x23 * (x31 * x44 - x34 * x41) + x24 * (x31 * x43 - x33 * x41)) \
              + x13 * (x21 * (x32 * x44 - x34 * x42) - x22 * (x31 * x44 - x34 * x41) + x24 * (x31 * x42 - x41 * x32)) \
              - x14 * (x21 * (x32 * x43 - x33 * x42) - x22 * (x31 * x43 - x33 * x41) + x23 * (x31 * x42 - x32 * x41))
        if det > maxdet:
            maxdet = det
            maxyear = x31 * 1000 + x32 * 100 + x33 * 10 + x34
            maxmonth = x41 * 10 + x42
            maxday = x43 * 10 + x44
        if det < mindet:
            mindet = det
            minyear = x31 * 1000 + x32 * 100 + x33 * 10 + x34
            minmonth = x41 * 10 + x42
            minday = x43 * 10 + x44
        wholedate = x31 * 10000000 + x32 * 1000000 + x33 * 100000 + x34 * 10000 + x41 * 1000 + x42 * 100 + x43 * 10 + x44

# print(det)
# print(x31, x32, x33, x34, x41, x42, x43, x44)
print("The date with the highest determinant is " + str(maxyear) + "/" + str(maxmonth) + "/" + str(maxday) + "!")
print("The highest determinant is:" + str(maxdet))
print("The date with the highest determinant is " + str(minyear) + "/" + str(minmonth) + "/" + str(minday) + "!")
print("The highest determinant is:" + str(mindet))