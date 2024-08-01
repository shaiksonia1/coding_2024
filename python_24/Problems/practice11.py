class Programmer:
    company = "Microsoft"

    def __init__(self,Name,employeeId,salary,Role):
        self.Name = Name
        self.employeeId = employeeId
        self.salary = salary
        self.Role = Role


sonia = Programmer("Sonia",2323,5000000,"Software Engineer")
print(sonia.company,sonia.salary,sonia.Role,sonia.Name)

            