class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.__salary = salary
        self.role = role

    @property
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, new_salary, by_role):
        if by_role.lower == "hr":
            self.__salary = new_salary
            print(f"salary increased to {new_salary} for {self.name} by {by_role}" )
        else:
            print(f"Only hr allowed to change the salary")