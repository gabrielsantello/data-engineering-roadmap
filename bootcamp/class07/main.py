from etl import filter_above

salary_list = [3000, 4000, 150000]
max_salary = 100000

print(filter_above(salary_list=salary_list, max_salary=max_salary))