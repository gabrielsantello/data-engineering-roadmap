import csv

from pydantic import validate_call

@validate_call
def read_csv_to_transform_into_dict(path: str) -> list[dict]:
    data = []
    with open(file=path, mode="r", encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Add each row (a dictionary) to the data list
            data.append(row)
    return data

@validate_call
def filter_delivered_products(lst=list[dict]) -> list[dict]:
    delivered_products_list = []
    for product in lst:
        if product.get("delivered") == "True":
            delivered_products_list.append(product)
    return delivered_products_list

@validate_call
def sum_values(lst=list[dict]) -> int:
    total_value = 0
    for product in lst:
        total_value += int(product.get("price"))
    return total_value

@validate_call
def pipeline(path: str):
    product_list = read_csv_to_transform_into_dict(path)
    delivered_products = filter_delivered_products(product_list)
    return sum_values(delivered_products)