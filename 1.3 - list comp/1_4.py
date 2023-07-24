

def combine_coins(symbol, number):
    return " ".join([symbol + str(x) + ',' for x in range(number)])


print(combine_coins('$', 5))
