
columns = ["A", "B", "C"]
cards   = 7
total   = columns * cards
test    = "3B"

data = {column: [] for column in columns}

for column in columns:
    i=1
    for _ in range(cards): 
        data[column].append(str(i)+column)
        i = i +1

for column, values in data.items():
    print(f"{column}: {values}")

for key, value in data.items():
    if test in value:
        print(key)

for key, value in data.items():
    print(value)

