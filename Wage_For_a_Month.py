import random
"""Calculate Wage for a Month"""
IS_PART_TIME = 1
IS_FULL_TIME = 2
EMP_RATE_PER_HOUR = 20
NUM_OF_WORKING_DAYS = 2
def CalculateWagesFor20DaysInMonth():
    empHrs = 0
    empWage = 0
    totalEmpWage = 0
    for i in range(0,NUM_OF_WORKING_DAYS):
        empCheck = random.randint(0, 3)
        if (empCheck==IS_PART_TIME):
            empHrs = 4
        elif(empCheck== IS_FULL_TIME):
            empHrs = 8
        else:
            empHrs = 0 
        empWage = empHrs * EMP_RATE_PER_HOUR
        totalEmpWage+=empWage
        print( totalEmpWage) 


if __name__=='__main__':        
    CalculateWagesFor20DaysInMonth()
