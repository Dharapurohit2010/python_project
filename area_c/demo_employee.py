class Employee:
    company_name=None #static variable or class variable
    company_location= None
    def __init__(self):
        self.emp_id=None#non-static variable or class-level
        self.emp_name=None
        self.emp_salary=None
        self.emp_performance=None
        self.__company_code=10   #private access modifier
        #self-to declare non static
    def company_code(self):
        return self.__company_code
    ##how to declare static method
    @staticmethod
    def print_authorname():
        print("Author name: ", "bala")
    def display_employee_record(self):
        print(35 *"---")
        print("Employee ID:" ,self.emp_id)
        print("Employee Name:" ,self.emp_name)
        print("Employee slary: " ,self.emp_salary)
        print("Employee Performance:" ,self.emp_performance)
        print("Company name:" ,Employee.company_name)
        print("Company location: ",Employee.company_location)
    @staticmethod
    def print_emp_id(employee):
        print("Author Name: ", "balaji dinakaran",employee.emp_id)
    def calculate_bonus(self):
        #self.display_employee_record()
        if self.emp_performance == "A":
            #print(self.emp_name)
            #print("10%")
            self.emp_salary=self.emp_salary + (self.emp_salary*10)/100
        elif self.emp_performance == "B":

            #print(self.emp_name)
            #print("5%")

            self.emp_salary = self.emp_salary + (self.emp_salary * 5 )/ 100
            print(self.emp_salary)
        elif self.emp_performance == "C":
            #print(self.emp_name)
            #print("2")
            self.emp_salary = self.emp_salary + (self.emp_salary * 5) / 100
        else:
            print(self.emp_name)
            print("No bonus")
            print(self.emp_salary)

