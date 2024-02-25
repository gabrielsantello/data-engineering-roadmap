def normalize_name(name: str) -> str:
    return name.strip().lower()

names = [" Alice ", "BOB", "Carlos"]
normalized_names = [normalize_name(name) for name in names]
print(normalized_names)