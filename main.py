import timeit, UTTest, Employee, logging

logging.basicConfig(filename="file.log", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.WARNING)

if __name__ == '__main__':

    beginningTime = timeit.default_timer()
    UTTest.UTTest().start_test()
    UTTest.UTTest().test_value()
    finalSalary = int(input("Enter final salary for the employee: "))
    numOfEmployees = int(input("Enter number of Employees: "))
    average = Employee.Employee().average_salary(finalSalary, numOfEmployees)
    print("Average Salary for Employee is ", average)
    firstPaycheck = int(input("Enter Salary for first paycheck: "))
    secondPaycheck = int(input("Enter Salary for second paycheck: "))
    thirdPaycheck = int(input("Enter Salary for third paycheck: "))
    total = Employee.Employee().final_salary(firstPaycheck, secondPaycheck, thirdPaycheck)
    print("Total Salary for Employee is ", total)
    finishingTime = timeit.default_timer()
    print(finishingTime - beginningTime)