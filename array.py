
columns = ["A", "B", "C"]
cards_per_column   = 7
total   = columns * cards_per_column
test    = "3B"
data = {column: [] for column in columns}

all_values = []

def init_dictionary (columns, cards_per_columns):
    data = {column: [] for column in columns}
    for column in columns:
        i=1
        for _ in range(cards_per_columns): 
            data[column].append(str(i)+column)
            i = i +1
    return data


def find_card_in_column (card, data):
    for key, value in data.items():
        if card in value:
            return key
    return None

data=init_dictionary(columns, cards_per_column)
print(data)
print(find_card_in_column(test,data))

def order_columns (correct_column, data):
    print(correct_column)
    for key, value in data.items():
        print(key)
        print(value)

print(order_columns("B",data))
for value in data.values():
    all_values.extend(value)
print(all_values)