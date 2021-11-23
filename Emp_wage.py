import random
"""Calculate Employee Wage"""
IS_PART_TIME = 1
IS_FULL_TIME = 2
EMP_RATE_PER_HOUR = 20
empHrs = 0
empWage = 0
empCheck = random.randint(0, 3)
if (empCheck==IS_PART_TIME):
    empHrs = 4
elif(empCheck== IS_FULL_TIME):
    empHrs = 8
else:
    empHrs = 0
empWage = empHrs * EMP_RATE_PER_HOUR
print(empWage)
