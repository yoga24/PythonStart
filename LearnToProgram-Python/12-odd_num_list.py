import random


def is_odd_present(num):
    if num % 2 != 0:
        return True
    return False


def get_odd_list(func, num_list):
    odd_list = []

    for num in num_list:
        if func(num):
            odd_list.append(num)

    return odd_list


no_list = random.sample(range(1, 100), 20)
print(no_list)
print(get_odd_list(is_odd_present, no_list))
