import logging, unittest


class Employee(unittest.TestCase):

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    def final_salary(self, first_paycheck, second_paycheck, third_paycheck):

        try:
            assert first_paycheck > 0
            assert second_paycheck > 0
            assert third_paycheck > 0
            self.assertLess(second_paycheck, third_paycheck, "second paycheck is lower.")
            self.assertGreater(first_paycheck, second_paycheck, "second paycheck is higher")
            final = first_paycheck+second_paycheck+third_paycheck
            self.logger.info("Salary of employee has been finalized")
            return final

        except:
            self.logger.warning("salary entered must be greater than 0")

    def average_salary(self, final_salary, num_of_employees):
        try:
            average = final_salary/num_of_employees
            self.logger.info("Average salary of employee has been finalized")
            return average
        except:
            self.logger.error("Employees should be more than 0")