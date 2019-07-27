

def get_item_index(array, key, value):
    for i in range(len(array)):
        if array[i][key] == value:
            return i
    return -1


def set_value_to_item(array, index, key, value):
    for i in range(len(array)):
        if i == index:
            array[i][key] = value
            break

    return array


def get_item_by_key_value(array, key, value):
    for item in array:
        if key in item and item[key] == value:
            return item

    return None
