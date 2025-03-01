columns = ["A", "B", "C"]
cards   = 7
test    = "3B"

data = {column: [] for column in columns}
for column in columns:
    i = 1
    for _ in range(cards): 
        data[column].append(str(i) + column)
        i += 1

for column, values in data.items():
    print(f"{column}: {values}")

for key, value in data.items():
    if test in value:
        print(f"El valor '{test}' se encuentra en la clave: {key}")

all_values = []
for value in data.values():
    all_values.extend(value)

print(all_values)
