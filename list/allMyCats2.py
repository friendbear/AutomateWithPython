
cat_names = []
while True:
    print('Please input cat name' + str(len(cat_names) + 1) +
          ' If exit Press Enter')
    name = input()

    if name == '':
        break
    cat_names = cat_names + [name]

print('printall')
for name in cat_names:
    print(name)

