import os

os.chdir('/tmp')

bacon_file = open('bacon.txt', 'w')
bacon_file.write('Hello world!\n')
bacon_file.close()


bacon_file = open('bacon.txt', 'a')
bacon_file.write('Bacon is not a vegetable.')
bacon_file.close()

bacon_file = open('bacon.txt', 'r')
for line in bacon_file.readlines():
    print(line)

bacon_file.close()

