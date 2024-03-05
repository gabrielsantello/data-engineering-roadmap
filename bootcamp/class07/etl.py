from pydantic import validate_call

@validate_call
def filter_above(salary_list: list[float], max_salary: float) -> list:
    above_salaries_list: list = []
    for salary in salary_list:
        if salary > max_salary:
            above_salaries_list.append(salary)
    return above_salaries_list