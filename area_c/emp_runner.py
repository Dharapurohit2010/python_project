from area_c.demo_employee import Employee

Employee.company_name = "Ifuture"
Employee.company_location = "pune"
print(Employee.company_name)
print(Employee.company_location)
emp_1 = Employee()
emp_2 = Employee()
emp_3 = Employee()

emp_2.emp_salary = 9000
print(type(emp_1))

###load emp1 data
emp_1.emp_id = "jsdf@gmail.com"
emp_1.emp_salary = 20000
emp_1.emp_performance = "B"

emp_1.emp_name = "Bob"

print(emp_1.emp_salary)
##how to call static method
Employee.print_authorname()

emp_1.display_employee_record()
emp_1.calculate_bonus()
print(emp_1.company_code())
