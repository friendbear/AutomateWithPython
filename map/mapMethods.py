

# map.values
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)

# map.keys
for k in spam.keys():
    print(k)

# map.items
for i in spam.items():
    print(i)

# for
for k, v in spam.items():
    print('key=' + k + ' value=' + str(v))

# exist
print('color' in spam.keys())
print('color' not in spam.keys())

# get
print(spam.get('noMapKey', 'defaultValue'))


