from fastapi import FastAPI
from faker import Faker
import pandas as pd
import random


app = FastAPI(debug=True)
fake = Faker()

file_name = 'data/products.csv'
df = pd.read_csv(file_name)
df['index'] = range(1, len(df) +1)
df.set_index('index', inplace=True)

defaultOnlineStore = 11

@app.get("/")
async def hello_world():
    return 'Coca-Cola sponsors me!'

@app.get("/generate_purchase")
async def generate_purchase():
    index = random.randint(1, len(df)-1)
    tuple = df.iloc[index]
    return [{
            "client": fake.name(),
            "creditcard": fake.credit_card_provider(),
            "product": tuple["Product Name"],
            "ean": int(tuple["EAN"]),
            "price":  round(float(tuple["Price"])*1.2,2),
            "clientPosition": fake.location_on_land(),
            "store": defaultOnlineStore,
            "dateTime": fake.iso8601()
        }]

@app.get("/generate_purchases/{number_of_records}")
async def generate_purchase(number_of_records: int):
    
    if number_of_records < 1:
        return {"error" : "The number must be greater than 1"}
 
    responses = []
    for _ in range(number_of_records):
        try:
            index = random.randint(1, len(df)-1)
            tuple = df.iloc[index]
            purchase = {
                    "client": fake.name(),
                    "creditcard": fake.credit_card_provider(),
                    "product": tuple["Product Name"],
                    "ean": int(tuple["EAN"]),
                    "price":  round(float(tuple["Price"])*1.2,2),
                    "clientPosition": fake.location_on_land(),
                    "store": defaultOnlineStore,
                    "dateTime": fake.iso8601()
                    }
            responses.append(purchase)
        except IndexError as e:
            print(f"Index error: {e}")
        except ValueError as e:
            print(f"Unexpected error: {e}")
            purchase = {
                    "client": fake.name(),
                    "creditcard": fake.credit_card_provider(),
                    "product": "error",
                    "ean": 0,
                    "price":  0.0,
                    "clientPosition": fake.location_on_land(),
                    "store": defaultOnlineStore,
                    "dateTime": fake.iso8601()
                    }
            responses.append(purchase)
        except Exception as e:
            print(f"Unexpected error: {e}")
    return responses