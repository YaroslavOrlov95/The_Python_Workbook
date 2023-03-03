dict_1 = {1:2, 3:4, 5:6, 7:8, 9:2, 10:2}
dict_2 = {1:2, 3:4, 5:6, 7:8, 9:10, 11:12}
dict_3 = {1:0, 3:4, 5:6, 7:8, 9:0, 10:0}

list_ = []
def reverseLookup(dict_, x, name):
    for k, v in dict_.items():
         if v == x:
             list_.append(k)
         else:
             pass
    print(f'в словаре с названием {name} -', *list_, f'- это ключи со значением {x}')
x = 2
reverseLookup(dict_1, x, "dict_1")

list_.clear()
reverseLookup(dict_2, x, "dict_2")
list_.clear()
reverseLookup(dict_3, x, "dict_3")
list_.clear()