import shelve

# create shelf 'mydata'
shelf_file = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']

shelf_file['cats'] = cats
shelf_file.close()

shelf_file = shelve.open('mydata')

for item in shelf_file['cats']:
    print(item)

shelf_file.close()


