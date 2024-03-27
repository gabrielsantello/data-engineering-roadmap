from datetime import datetime

def greet_person(person):
    return f'Hello, {person["name"]}!'

def birth_year_person(person):
    current_year = datetime.now().year
    age = int(person["age"])
    birth_year = current_year - age
    return f'You were born in: {birth_year}'

def job_status(person):
    if person["profession"] == "Data Eng":
        return f'Sorry, no openings for: {person["profession"]}'
    return f'I will find you a job as a {person["profession"]}'

person1 = {
    "name": "Fabio",
    "age": "35",
    "profession": "Data Eng"
}

person2 = {
    "name": "Luciano",
    "age": "33",
    "profession": "Data Product Manager"
}

print(person1)
print(greet_person(person1))
print(birth_year_person(person1))
print(job_status(person1))

print(person2)
print(greet_person(person2))
print(birth_year_person(person2))
print(job_status(person2))