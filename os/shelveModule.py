import shelve

# create shelf 'mydata'
shelf_file = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']

shelf_file['cats'] = cats
shelf_file.close()

shelf_file = shelve.open('mydata')

for item in shelf_file['cats']:
    print(item)

for key in shelf_file.keys():
    for value in shelf_file[key]:
        print(key + '=' + value)


shelf_file.close()


