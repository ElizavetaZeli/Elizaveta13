calls = 0
def count_calls ():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return any(item.lower() == string.lower() for item in list_to_search)

string_result = string_info('Hello')
print(string_result)

list_check = ["apple", "banana", "urban"]
contains_result = is_contains("UrbaN", list_check)
print(contains_result)

print(f"Количество вызовов: {calls}")