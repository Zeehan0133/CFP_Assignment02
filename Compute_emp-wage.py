import random
"""Store the Daily Wage along with the Total Wage"""
IS_PART_TIME = 1
IS_FULL_TIME = 2
def ComputeEmpWage( company,  empRatePerHour,  numOfWorkingDays,  maxHoursPerMonth):
    empHrs = 0
    totalEmpHrs = 0
    totalWorkingDays = 0
    while (totalEmpHrs <= maxHoursPerMonth and totalWorkingDays < numOfWorkingDays):
        totalWorkingDays+=1
        empCheck = random.randint(0, 3)
        if (empCheck==IS_PART_TIME):
            empHrs = 4
        elif(empCheck== IS_FULL_TIME):
            empHrs = 8
        else: 
            empHrs = 0 
        totalEmpHrs += empHrs
    totalEmpWage = totalEmpHrs * empRatePerHour
    print("Total Emp Wage for company: " + str(company) + " is : " + str(totalEmpWage))
    return totalEmpWage

if __name__=='__main__': 
    ComputeEmpWage("Airtel", 2, 10, 20)
