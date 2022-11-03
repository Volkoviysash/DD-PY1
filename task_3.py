import random


def get_unique_list_numbers() -> list[int]:
    list_ = []
    while len(list_) < 15:
        number = random.randint(-10, 10)
        if number not in list_:
            list_.append(number)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
