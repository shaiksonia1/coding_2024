class Programmer:
    company = "Microsoft"

    def __init__(slf,Name,employeeId,salary,Role):
        slf.Name = Name
        slf.employeeId = employeeId
        slf.salary = salary
        slf.Role = Role


sonia = Programmer("Sonia",2323,5000000,"Software Engineer")
print(sonia.company,sonia.salary,sonia.Role,sonia.Name)

            # we can put any name in the place of self like slf, sonia, but it is not a good practice for the programmers