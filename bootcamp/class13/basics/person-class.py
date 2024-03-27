from datetime import datetime

class Person:
    def __init__(self, name, age, profession):
        self.name = name
        self.age = age
        self.profession = profession

    def greet(self):
        return f'Hello, {self.name}!'

    def birth_year(self):
        current_year = datetime.now().year
        birth_year = current_year - int(self.age)
        return f'You were born in: {birth_year}'

    def job_status(self):
        if self.profession == "Data Eng":
            return f'Sorry, no openings for: {self.profession}'
        return f'I will find you a job as a {self.profession}'

# Example usage:
person1 = Person("Fabio", "35", "Data Eng")
person2 = Person("Luciano", "33", "Data Product Manager")
print(person1.greet())
print(person1.birth_year())
print(person1.job_status())

print(person2.greet())
print(person2.birth_year())
print(person2.job_status())