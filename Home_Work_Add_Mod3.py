# "Подробнее о функциях." Доп. практическое задание по 3 модулю.
# Задание: "Раз, два, три, четыре, пять .... Это не всё?"

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
    ca_st_sum = calculate_structure_sum
    dat_str = data_structure
    summa = 0
    if dat_str == []:
        return summa
    if isinstance(dat_str, dict):
        for key, value in dat_str.items():
            summa += ca_st_sum(key)
            summa += ca_st_sum(value)
    elif isinstance(dat_str, (tuple, set, list)):
        for i in dat_str:
            summa += ca_st_sum(i)
    elif isinstance(dat_str, (int, float)):
        summa += dat_str
    elif isinstance(dat_str, str):
        summa += len(dat_str)
    return summa


result = calculate_structure_sum(data_structure)
print('Cумма всех чисел и длина всех строк: ', result)



