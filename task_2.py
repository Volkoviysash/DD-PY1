number_of_characters = {}

def get_count_char(str_):
    str_ = str_.lower()
    for char_ in str_:
        # Для каждого символа в строке, который является буквой и не описан в словаре
        if char_.isalpha() and (char_ not in number_of_characters):
            number_of_characters[char_] = str_.count(char_)
    return number_of_characters


def get_percent_count_char(number_of_characters):
    percent_count_char = {}
    for char_ in number_of_characters:
        # Разделить его значение на сумму всех значений всех ключей словаря, умножить на 100% и округлить до целых
        percent_count_char[char_] = round(number_of_characters[char_] / sum(number_of_characters.values()) * 100)
    return percent_count_char

main_str = "Данное предложение будет разбиваться на отдельные слова. В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!"

print(get_count_char(main_str))
#print(get_percent_count_char(number_of_characters))
