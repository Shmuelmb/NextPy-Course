
def divider(num):
    return num % 4 == 0

def four_dividers(number: int):
    return list(filter(divider,range(1,number+1)))
  
print(four_dividers(12))