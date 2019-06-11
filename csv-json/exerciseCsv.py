#! python3

import csv
import setup

example_file = open('example.csv')


# reader is iterative
example_reader = csv.reader(example_file)

for row in example_reader:
    print('Row#{} {}'.format(example_reader.line_num, str(row)))


# writer
delimiter = {'csv': ',', 'tsv': '\t'}

for k, v in delimiter.items():
    output_file = open('output.{}'.format(k), 'w', newline='')
    output_writer = csv.writer(output_file, delimiter=v) # delimiter=','

    output_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
    output_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
    output_writer.writerow([1, 2, 3.141592, 4])

    output_file.close()

