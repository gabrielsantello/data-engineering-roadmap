from typing import Dict, Optional, Any

import json

lists: Any = ["Shoe", 39, 10.38, True]

product_01: Dict[str, Any] = {
    "name":"Shoe",
    "quantity":39,
    "price": 10.38,
    "availability": True
}

product_02: dict = {
    "name":"Television",
    "quantity":10,
    "price": 70.44,
    "availability": False
}

cart: list = []

cart.append(product_01)
cart.append(product_02)

cart_json = json.dumps(cart)
print(cart_json)