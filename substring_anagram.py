# substring anagram in a given string with all matches
def substring_anagram(dictionary: list, sub: list) -> None:
    print(dictionary)
    print(sub)
    return sub


all_word = ['abc', 'a', 'bca', 'abcd', 'dac', 'acd']
query = ['abc', 'a', 'ada']

out_list = substring_anagram(all_word, query)
print(out_list)



