class EmployeeSalary:

    hourly_payment = 400
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email, hours = None):
        if hours == None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, rest_days, hours, email = None):
        if email == None:
            email = f"{name}@email.com"

        return cls(name, hours, rest_days, email)
    
    @classmethod
    def set_hourly_payment(cls, hourly_payment):
        cls.hourly_payment = hourly_payment

    def salary(self):
        return self.hours * self.hourly_payment
    
    def __str__(self):
        return f"name={self.name} hours={self.hours} rest_days={self.rest_days} email={self.email} hourly_payment={self.hourly_payment}"
    
employeeSalary1 = EmployeeSalary.get_hours(name = 'Наталия', rest_days = 2, email = 'hello@gmail.com')
print(employeeSalary1)
employeeSalary2 = EmployeeSalary.get_hours(name = 'Наталия', rest_days = 2, email = 'hello@gmail.com', hours = 30)
print(employeeSalary2)
employeeSalary3 = EmployeeSalary.get_email(name = 'Наталия', rest_days = 2, hours = 40)
print(employeeSalary3)
employeeSalary4 = EmployeeSalary.get_email(name = 'Наталия', rest_days = 2, hours = 50, email = 'hello@gmail.com')
print(employeeSalary4)
EmployeeSalary.set_hourly_payment(300)
print(employeeSalary1.salary())
print(employeeSalary2.salary())
print(employeeSalary3.salary())
print(employeeSalary4.salary())
