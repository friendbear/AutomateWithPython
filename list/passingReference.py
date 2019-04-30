
def eggs(some_parameter):
    some_parameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)

if 'Hello' in spam:
    print("Yes !")
print(spam)
