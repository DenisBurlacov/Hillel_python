# 1. Створити простий, пустий клас без реалізації - PlaceHolder

class PlaceHolder:
    pass


# 2. Створити клас який приймає при ініціалізації 1 параметр і додати метод який друкує цей параметр

class Employee:
    employee_id = 0  # 3. Додати до класу з пункту 2 змінну класу

    def __init__(self, employee_name):
        self.employee_name = employee_name
        Employee.employee_id += 1

    def print_employee_name(self):
        print(f'The employee name is: {self.employee_name}')

    @staticmethod  # 3. Додати до класу з пункту 2 статичний метод
    def get_employee_id():
        return Employee.employee_id


# 4. Створити клас який успадковується від класу з пункта 2.
# Додади для ініціалізації ще 1 параметр і ще один метод для виведення нового параметра.

class EmployeeProfession(Employee):
    def __init__(self, employee_name, employee_profession):
        Employee.__init__(self, employee_name)
        self.employee_profession = employee_profession

    def print_employee_profession(self):
        print(f'The employee profession is: {self.employee_profession}')


employee_first = Employee('Denis')
employee_first.print_employee_name()
print(f'The employee id is: {employee_first.employee_id}')
print('*' * 25)
print()

employee_second = EmployeeProfession('Denys_2', 'QA')
employee_second.print_employee_name()
print(f'The employee id is: {employee_second.employee_id}')
employee_second.print_employee_profession()
