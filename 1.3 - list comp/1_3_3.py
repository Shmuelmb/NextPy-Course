def is_funny(string):
    # [i != "a" and i != "h" for i in string]  - return list with True where the string have char that is not a or h
    return False in [i != "a" and i != "h" for i in string] and True not in [i != "a" and i != "h" for i in string]


print(is_funny('hahahahahahahahaha'))

# more func by chatgpt
# def is_funny(string):
#     return all(char == 'a' or char == 'h' for char in string)
def 