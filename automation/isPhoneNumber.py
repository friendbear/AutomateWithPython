
import re

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # 3桁の市外局番(()がついても良い)
    (\s|-|\.)?         # 区切り
    \d{3}              # 3桁の市内局番
    (\s|-|\.)          # 区切り
    \d{4}              # 4桁の番号
    (\s*(ext|x|ext.)\s*\d{2,5})? # 2-5桁の内線番号
    )''', re.VERBOSE)

def is_phone_number(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

def is_phone_number_with_regex(text):
    # phone_num_regex = re.compile(r'([0-9]{3}-[0-9]{3}-[0-9]{4})')
    no = phone_regex.search(text) # => Match Object

    return no != None

def find_phone_number(text):
    for i in range(len(text)):
        chunk = text[i:i+12]
        if is_phone_number(chunk):
            return True
    return False

def findall_phone_number_with_regex(text):

    return phone_regex.findall(text)


# Test Code
print(is_phone_number('415-555-4242'))
print(is_phone_number('abcccccccccc'))

print(is_phone_number_with_regex('415-555-4242'))
print(is_phone_number_with_regex('abcccccccccc'))

message = 'abcke415-444-2222kkeafe032-039-9283--'
print(find_phone_number(message))

# list and tuple
nums: (str, str, str) = findall_phone_number_with_regex(message)
for n in nums:
    for i in list(n):
        print(i)


