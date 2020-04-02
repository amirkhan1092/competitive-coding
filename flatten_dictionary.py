#
# This problem was asked by Stripe.
# Write a function to flatten a nested dictionary. Namespace the keys with a period.
# For example, given the following dictionary:
# {     "key": 3,     "foo": {         "a": 5,         "bar": {             "baz": 8         }     } }
# it should become:
# {     "key": 3,     "foo.a": 5,     "foo.bar.baz": 8 }
# You can assume keys do not contain dots in them, i.e. no clobbering will occur


# data_dict = eval(input())  # enter nested dictionary
data_dict = {     "key": 3,     "foo": {         "a": 5,         "bar": {             "baz": 8         }     } }

res_dict = {}
data_lst = list(data_dict.items())
print(data_lst)  # [('key', 3), ('foo', {'a': 5, 'bar': {'baz': 8}})]

for i, j in data_lst:
    tpl = []
    if type(j) != dict:
        tpl.append(i)
        res_dict['.'.join(tpl)] = j
        data_lst.remove((i, j))


    while 1:
        for i, j in data_lst.copy():
            if type(j) != dict:
                tpl.append(i)
                res_dict['.'.join(tpl)] = j
                data_lst.remove((i, j))
                data_lst.insert(0, list(j.items))
    print(res_dict)


def gg(g):
    for i in s:
        max(i, key= len)

lst = [['zs', 'gg'], ['abcf', 'hgg']]

k = lambda x: max([i for h in x for i in h], key=lambda tt:len(tt))

print(k(lst))