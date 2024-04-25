class Manager(Employee):
    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")
