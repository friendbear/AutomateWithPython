
while True:
    print('who is this')
    name = input()
    if name != 'Joe':
        continue
    print('Hello Joe. press password')
    password = input()
    if password == 'sordfish':
        break

print('authorized')
