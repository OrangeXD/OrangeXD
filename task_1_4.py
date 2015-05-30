def one(string, dict):
    if dict.has_key(string) is True:
        value = dict[string]
        del dict[string]
        dict['None'] = value
    print dict

dict = {
        'one': 1, 'two': 2
    }
one('one', dict)

def two(dict_1, dict_2):
    for key in dict_2:
        if dict_1.has_key(key) is True:
            del dict_1[key]
            del dict_2[key]
            break
    dict_1.update(dict_2)
    print dict_1

dict_1 = {
        'one': 1, 'three': 3
    }
dict_2 = {
        'one': 1, 'two': 2
    }
two(dict_1, dict_2)

def calculate(one, two, three):
    dictionary = {
        'add': '+',
        'min': '-',
        'umn': '*',
        'del': '/'
    }
    dicti = {}
    dicti['one'] = one
    dicti['two'] = two
    oper = dictionary.get(three)
    rez = one + oper + two
    print rez

calculate(1, 2, 'add')

def four(dict_3):
    dic = {}
    for key in dict_3:
        value = dict_3[key]
        dic[value] = key
    print dic

dict_3 = {'one': 1, 'two': 2}
four(dict_3)