
def dict_key_is_empty(key, dict_data):
    if key not in dict_data:
        return True
    elif dict_data[key] is None:
        return True
    else:
        return False
