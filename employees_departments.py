import datetime

class Employee:

    def __init__(self, name, title, start):
        self.name = name
        self.job_title = title
        self.employment_start_date = start

class Company:

    def __init__(self, name, address, industry):
        self.business_name = name
        self.address = address
        self.industry_type = industry
        self.employees = list()


tony = Employee("Tony Stark", "Owner", datetime.datetime.now())
pepper = Employee("Pepper Potts", "CEO", datetime.datetime.now())

peter = Employee("Peter Parker", "Spiderman", datetime.datetime.now())
thor = Employee("Thor, Son of Odin", "God of Thunder", datetime.datetime.now())
steve = Employee("Steve Rogers", "Captain America", datetime.datetime.now())

stark_industries = Company("Stark Industries", " New York City", "Defense")
stark_industries.employees.append(tony)
stark_industries.employees.append(pepper)


avengers = Company("Avengers", "Upstate New York", "Defense")


avengers.employees.append(peter)
avengers.employees.append(thor)
avengers.employees.append(steve)

# print(avengers)
# print(stark_industries)
companies = []
companies.append(stark_industries)
companies.append(avengers)

for company in companies:
    print(f'{company.business_name} is in the {company.industry_type} industry and has the following employees:')
    for employee in company.employees:
        print(f' * {employee.name}')
