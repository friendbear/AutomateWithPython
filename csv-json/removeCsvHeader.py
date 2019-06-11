#! python3

import csv, os
import setup

os.makedirs('headerRemoved', exist_ok=True)

for csv_filename in os.listdir('.'):
    if csv_filename.endswith('.csv'):

        csv_rows = []
        csv_file_obj = open(csv_filename, 'r')
        reader_obj = csv.reader(csv_file_obj)
        for row in reader_obj:
            if reader_obj.line_num == 1:
                continue
            csv_rows.append(row)
        csv_file_obj.close()


        csv_file_obj = open(os.path.join('headerRemoved', csv_filename), 'w', newline='')

        csv_writer = csv.writer(csv_file_obj)

        for row in csv_rows:
            csv_writer.writerow(row)
        csv_file_obj.close()


