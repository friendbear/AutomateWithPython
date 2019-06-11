#! python3

import PyPDF2
import setup

pdf_file_obj = open('meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
num = pdf_reader.getNumPages()
dictionary = {}

for p in range(0, num):
    for line in pdf_reader.getPage(p).extractText().split('\s|\n'):
        print(line)


