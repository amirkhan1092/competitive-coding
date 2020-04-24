# substring anagram in a given string with all matches
def substring_anagram(dictionary: list, sub: list) -> None:
    dictionary_sort = list(map(sorted, dictionary))
    sub_sort = map(sorted, sub)
    m = []
    for i in sub_sort:
        m.append(dictionary_sort.count(i))

    return m



#
# all_word = ['abc', 'a', 'bca', 'abcd', 'dac', 'acd']
# query = ['abc', 'a', 'ada']

all_word = eval(input())  # user having all anagram pattern
query = eval(input())  # user enter the sublist
out_list = substring_anagram(all_word, query)
print(out_list)
