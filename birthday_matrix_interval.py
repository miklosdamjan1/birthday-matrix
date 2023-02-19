# Asks for the matrix.
a = maxdet = maxyear = maxmonth = maxday = maxstartyear = maxstartmonth = maxstartday = mindet = minyear = minmonth = 0
minday = minstartyear = minstartmonth = minstartday = 0
wholedate = x = input("From what date do you want to start th calculation?(format: YYYYMMDD)")
original = startdate = int(x)
# Asks how many years to calculate.
duration = input("How many years after that date do you want to calculate?")
eachduration = input("For each date how many years do you want to calculate?")
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
# min-max determinant of the next "duration years
while True:
    if int(startdate) >= original + int(duration) * 10000:
        break
    else:
        while True:
            if int(wholedate) >= int(startdate) + int(eachduration) * 10000:
                if x12 == x13 == x14 == 9 and x21 == 1 and x22 == 2 and x23 == 3 and x24 == 1:
                    x11 = x11 + 1
                    x12 = x13 = x14 = x24 = x21 = x23 = 0
                    x22 = 1
                if x13 == x14 == 9 and x21 == 1 and x22 == 2 and x23 == 3 and x24 == 1:
                    x12 = x12 + 1
                    x13 = x14 = x21 = x23 = x24 = 0
                    x22 = 1
                if x14 == 9 and x21 == 1 and x22 == 2 and x23 == 3 and x24 == 1:
                    x13 = x13 + 1
                    x14 = x21 = x24 = x23 = 0
                    x22 = 1
                if x21 == 1 and x22 == 2 and x23 == 3 and x24 == 1:
                    x14 = x14 + 1
                    x21 = x23 = x24 = 0
                    x22 = 1
                if x22 == 9 and x23 == 3 and x24 == 0:
                    x21 = 1
                    x22 = x23 = x24 = 0
                if ((x21 == 1 and (x22 == 2 or x22 == 0)) or (
                        x21 == 0 and (
                        x22 == 1 or x22 == 3 or x22 == 5 or x22 == 7 or x22 == 8))) and x23 == 3 and x24 == 1:
                    x22 = x22 + 1
                    x23 = 0
                    x24 = 0
                if (x21 == x22 == 1) and x23 == 3 and x24 == 0:
                    x22 = x22 + 1
                    x23 = 0
                    x24 = 0
                if (x21 == 0 and (x22 == 4 or x22 == 6)) and x23 == 3 and x24 == 0:
                    x22 = x22 + 1
                    x23 = 0
                    x24 = 0
                if ((x11 * 1000 + x12 * 100 + x13 * 10 + x14) % 4 == 1 or (
                        x11 * 1000 + x12 * 100 + x13 * 10 + x14) % 4 == 2 or (
                            x11 * 1000 + x12 * 100 + x13 * 10 + x14) % 4 == 3) and x21 == 0 and x22 == x23 == 2 and x24 == 8:
                    x22 = x22 + 1
                    x23 = 0
                    x24 = 0
                if x21 == 0 and x22 == x23 == 2 and x24 == 9:
                    x22 = x22 + 1
                    x23 = 0
                    x24 = 0
                x24 = x24 + 1
                if x24 == 10:
                    x23 = x23 + 1
                    x24 = 0
                startdate = x11 * 10000000 + x12 * 1000000 + x13 * 100000 + x14 * 10000 + x21 * 1000 + x22 * 100 + x23 * 10 + x24

                x31 = x11
                x32 = x12
                x33 = x13
                x34 = x14
                x41 = x21
                x42 = x22
                x43 = x23
                x44 = x24
                wholedate = x31 * 10000000 + x32 * 1000000 + x33 * 100000 + x34 * 10000 + x41 * 1000 + x42 * 100 + x43 * 10 + x44
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
                        x41 == 0 and (
                        x42 == 1 or x42 == 3 or x42 == 5 or x42 == 7 or x42 == 8))) and x43 == 3 and x44 == 1:
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
                det = x11 * (x22 * (x33 * x44 - x34 * x43) - x23 * (x32 * x44 - x34 * x42) + x24 * (
                        x32 * x43 - x33 * x42)) \
                      - x12 * (x21 * (x33 * x44 - x34 * x43) - x23 * (x31 * x44 - x34 * x41) + x24 * (
                        x31 * x43 - x33 * x41)) \
                      + x13 * (x21 * (x32 * x44 - x34 * x42) - x22 * (x31 * x44 - x34 * x41) + x24 * (
                        x31 * x42 - x41 * x32)) \
                      - x14 * (x21 * (x32 * x43 - x33 * x42) - x22 * (x31 * x43 - x33 * x41) + x23 * (
                        x31 * x42 - x32 * x41))
                if det > maxdet:
                    maxdet = det
                    maxyear = x31 * 1000 + x32 * 100 + x33 * 10 + x34
                    maxmonth = x41 * 10 + x42
                    maxday = x43 * 10 + x44
                    maxstartyear = x11 * 1000 + x12 * 100 + x13 * 10 + x14
                    maxstartmonth = x21 * 10 + x22
                    maxstartday = x23 * 10 + x24
                if det < mindet:
                    mindet = det
                    minyear = x31 * 1000 + x32 * 100 + x33 * 10 + x34
                    minmonth = x41 * 10 + x42
                    minday = x43 * 10 + x44
                    minstartyear = x11 * 1000 + x12 * 100 + x13 * 10 + x14
                    minstartmonth = x21 * 10 + x22
                    minstartday = x23 * 10 + x24
                wholedate = x31 * 10000000 + x32 * 1000000 + x33 * 100000 + x34 * 10000 + x41 * 1000 + x42 * 100 + x43 * 10 + x44

# print(det)
# print(x31, x32, x33, x34, x41, x42, x43, x44)
print("The date with the highest determinant is " + str(maxyear) + "/" + str(maxmonth) + "/" + str(maxday) + "!")
print("The highest determinant is:" + str(maxdet))
print("The birthday for the highest determinant is:" + str(maxstartyear) + "/" + str(maxstartmonth) + "/" + str(
    maxstartday) + "!")
print("The date with the lowest determinant is " + str(minyear) + "/" + str(minmonth) + "/" + str(minday) + "!")
print("The lowest determinant is:" + str(mindet))
print("The birthday for the lowest determinant is:" + str(minstartyear) + "/" + str(minstartmonth) + "/" + str(
    minstartday) + "!")
