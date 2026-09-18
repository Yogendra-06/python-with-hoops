class Employee:
    employee_id = 6621
    name = "rakesh"
    basic_salary = 100000
    
    def total_salary(self):
        HRA = 0.2 * self.basic_salary  
        DA = 0.1 * self.basic_salary
        total = self.basic_salary + HRA + DA
        print("Total Salary:", total)  

s = Employee()
print(s.employee_id)
print(s.name)
print(s.basic_salary)

s.total_salary()   
