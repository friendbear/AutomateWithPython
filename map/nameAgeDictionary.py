
print('Name: Age Example')
ages = {'tom': 25, 'alice': 29, 'jone': 18}
while True:
    print('Please input your name?  if exit. press enter')
    name = input()
    if name == '':
        break

    if name in ages:
        print(name + 's age is' + ages[name])
    else:
        print(name + 's age is not regist. Please enter age')
        birthday = int(input())
        ages[name] = birthday

print(ages)
