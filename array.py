
columns             = ["A", "B", "C"]
cards_per_column    = 9
total               = columns * cards_per_column
test                = "4C"
all_values          = []
debug               = False   

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

def find_card_position(card, data):
    for key, value in data.items():
        if card in value:
            return value.index(card)
    return None 

def order_columns (correct_column, data):
    keys = list(data.keys())
    correct_index = keys.index(correct_column)
    middle_index = len(keys) // 2
    keys.pop(correct_index)
    keys.insert(middle_index, correct_column)
    ordered_data = {key: data[key] for key in keys}
    return ordered_data


def get_all_values(ordered_data):
    for value in ordered_data.values():
        all_values.extend(value)
    return all_values

def recreate_data(columns, cards_per_column, test):
    data = init_dictionary(columns, cards_per_column)
    column_key = find_card_in_column(test, data)
    ordered_data = order_columns(column_key, data)
    all_values = get_all_values(ordered_data)
    recreated_data = {column: [] for column in columns}
    index = 0
    for i in range(cards_per_column):
        for col in columns:
            recreated_data[col].append(all_values[index])
            index += 1
    
    return recreated_data

data=init_dictionary(columns, cards_per_column)
if debug:
    print(data)

all_values=(get_all_values(data))

for value in all_values:
    print ("Test card: " + value)
    test = value

    for i in range(8):
        column_key= find_card_in_column(test,data)
        card_position=str((find_card_position(test,data)))
        print("Iteration nº" + str(i))
        print("Test card is in column " + column_key + " in position " + card_position)
        ordered_data = order_columns(column_key,data)
        if debug:
            print(ordered_data)
        all_values = []
        all_values=(get_all_values(ordered_data))
        if debug:
            print(all_values)
        data = recreate_data(columns, cards_per_column, test)
        if debug:
            print(data)

