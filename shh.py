class Employee:
    def __init__(self, employee_id, name, age, salary):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}\t{self.name}\t{self.age}\t{self.salary}"


class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def display_table(self):
        print("Employee ID\tName\tAge\tSalary")
        for employee in self.employees:
            print(employee)


if __name__ == "__main__":
    # Sample data
    employees_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000),
    ]

    # Create an EmployeeTable
    employee_table = EmployeeTable(employees_data)

    # Display the table
    print("\nEmployee Table:")
    employee_table.display_table()
