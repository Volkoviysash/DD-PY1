import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimeter=",", new_line="\n") -> list[dict]:
    with open(filename, "r") as file:
        data = file.readlines()
        # Разделяем заголовки от данных
        headers = data[0].replace(new_line, "").split(delimeter)  # убираем знак новой строки и создаем список элементов
        lines_of_values = data[1:]
        # Создаем будущий список всех обьектов
        list_of_objects = []
        # Каждая строчка - это набор параемтров отдельного объекта
        for line in lines_of_values:
            object_values = line.replace(new_line, "").split(delimeter)  # убираем знак новой строки и создаем список элементов
            list_of_objects.append(dict(zip(headers, object_values)))

        return list_of_objects


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
