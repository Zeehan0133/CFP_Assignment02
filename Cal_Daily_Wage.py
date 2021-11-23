import random
"""Calculate Daily Wage of the Employee """
IS_FULL_TIME = 1
Emp_Rate_Per_Hur = 20
Emp_Hur=0
Emp_Wage=0
empCheck = random.randint(0, 2)
if empCheck == IS_FULL_TIME:
    Emp_Hur=8
else:
    Emp_Hur=0
Emp_Wage= Emp_Hur * Emp_Rate_Per_Hur
print( Emp_Wage)     
