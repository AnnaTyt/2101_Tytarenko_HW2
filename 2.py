# ТЗ: В строке текста записаны слова, разделенные пробелами в произвольном количестве.
# Сжатие текста состоит в том, что между словами остается по одному пробелу,
# а после последнего слова пробелы удаляются (пробелы перед первым словом сохраняются).
# Если строка содержит только пробелы, то все они сохраняются.

# Developer notes: Для выполнения данной задачи используйте циклы.
# У строк есть методы "some_string".strip(), "some_string".lstrip(), "some_string".rstrip()
# они позволяют избавляться от пробелов в строках. Используйте этот инструментарий.
# Можете и спользовать конкатенацию строк.

# Входные данные:
# test_str_1 = "  Hello world   this is   me   "
# test_str_2 = "Hello world   this is   me again   "
# test_str_3 = "      "
# test_str_4 = "   Hello world   this is  not actually me   :)"

# На выходе должно быть:
# test_str_1 = "  Hello world this is me"
# test_str_2 = "Hello world this is me again"
# test_str_3 = "      "
# test_str_4 = "   Hello world this is not actually me :)"


test_string = input("Please enter string >> ")

if test_string.isspace():  # проверяем на пробелы
    pass
else:
    test_string = test_string.rstrip()

res_string = ""
ex_1 = False
ex_2 = False

for i in test_string:
    if i == " " and not ex_1:
        res_string += i
    elif i == " " and ex_1 and not ex_2:
        ex_2 = True
        res_string += i
    elif i != " ":
        ex_1 = True
        ex_2 = False
        res_string += i

print(f"'{res_string}'")
