from typing import List, Union

data: List[str] = ['Data'] * 3
data.append('appendData')
data.index('appendData')
data.insert(1, 'head')
print(data)

# sort
# basic
spam: List[Union[int, float]] = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam.sort(reverse=True)
print(spam)

# TODO:
def str_sort(data: List[str]):
    if(len(data) != 0):
        data.sort

print(str_sort(['hello', 'python']))
