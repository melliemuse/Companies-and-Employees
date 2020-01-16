# Instructions
# Create an Employee type that contains information about employees of a company. Each employee must have a name, job title, and employment start date.

class Employee:
    def __init__(self, name, title, date):
        self.name = name
        self.job_title = title
        self.start_date = date

# Create a Company type that employees can work for. A company should have a business name, address, and industry type.

class Company:
    def __init__(self, name):
        self.business_name = name
        self.address = ""
        self.industry_type = ""
        self.employees = list()
    def add_employee(self, new_employee):
        self.employees.append(new_employee.name)

# Create two companies, and 5 people who want to work for them.

business1 = Company("Genero-Corps")
business1.industry = "generic"
business2 = Company("Ink.inc")
business2.industry = "publishing"

employee1 = Employee("Peggy-Lu", "Project Lead", "December 27, 2019")
employee2 = Employee("Marty Bauman", "Consultant", "December 7, 2047")
employee3 = Employee("Mack the Knife", "Singer", "1900")
employee4 = Employee("Stacy", "Dev Ops", "October 31st, 2019")
employee5 = Employee("Colonel Sanders", "Engineer", "2050")

# Assign 2 people to be employees of the first company.

business1.add_employee(employee4)
business1.add_employee(employee2)

# Assign 3 people to be employees of the second company.

business2.add_employee(employee5)
business2.add_employee(employee3)
business2.add_employee(employee1)

# Output a report to the terminal the displays a business name, and its employees.
# For example: 

# Acme Explosives is in the chemical industry and has the following employees
#    * Michael Chang
#    * Martina Navritilova

# Jetways is in the transportation industry and has the following employees
#    * Serena Williams
#    * Roger Federer
#    * Pete Sampras

def print_business_info(company):
    print(f"{company.business_name} is in the {company.industry} industry and has the following employees")
    for employee in company.employees:
        print(f"{employee}")

print_business_info(business1)
print_business_info(business2)