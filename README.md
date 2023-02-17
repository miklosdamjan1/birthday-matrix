# birthday-matrix
This python code calculates the lowest and highest determinant of a birthday matrix until a specified date.
I define the birthday matrix as a 4x4 matrix where the first line is the year you were born, the second line is the month and day part of your birthday. The 3rd and 4th line is the same format but with the current date instead of your birthday. Each day there is a different matrix with a different determinant.
The matrix looks like this:
YYYY
MMDD
YYYY
MMDD
I did not use functions for this because as tested it resulted in a much higher calculation time. This way it can calculate each days determinant for a million years in about 10 minutes.
