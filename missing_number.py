# enter the list by user
# using list comprehension
lst = eval(input())
out = [i for i in range(lst[0], lst[-1]+1) if i not in lst]
print(out)


# using append
lst = eval(input())
out = []
for i in range(lst[0], lst[-1]+1):
    if i not in lst:
        out.append(i)
print(out)



