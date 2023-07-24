import functools
def add(x):
    return x + x

def double_letter(my_str):
    return ''.join(map(add, my_str))


print(double_letter('shmuel'))
