def get_count_char(str_):
     # TODO посчитать количество каждой буквы в строке в аргументе str_
     my_dict = {}
     new_str = str_.lower()
     DEFAULT_NUMBER = 0
     for symb in new_str:
          if symb.isalpha():
               my_dict[symb] = my_dict.get(symb, DEFAULT_NUMBER) + 1
     return (my_dict)

def percent_symbols(dictionary):
       percent = {}
    for key in dictionary.keys():
       percent[key] = round(dictionary.get(key) / sum(dictionary.values()) * 100, 2)
    return percent

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(percent_symbols(get_count_char(main_str)))
