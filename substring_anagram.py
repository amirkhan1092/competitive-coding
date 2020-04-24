# substring anagram in a given string with all matches
def substring_anagram(dictionary: list, sub: list) -> None:
    dictionary_sort = list(map(sorted, dictionary))
    sub_sort = map(sorted, sub)

    print(sub)
    return sub


all_word = ['abc', 'a', 'bca', 'abcd', 'dac', 'acd']
query = ['abc', 'a', 'ada']

out_list = substring_anagram(all_word, query)
print(out_list)



