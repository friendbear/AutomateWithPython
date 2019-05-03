
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

def find_phone_number(text):
    for i in range(len(text)):
        chunk = text[i:i+12]
        if is_phone_number(chunk):
            return True
    return False

print(is_phone_number('415-555-4242'))
print(is_phone_number('abcccccccccc'))

message = 'abcke415-444-2222kkeafe'
print(find_phone_number(message))


