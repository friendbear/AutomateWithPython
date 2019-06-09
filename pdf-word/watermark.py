#! python3

import PyPDF2
import setup
minutes_file = open('meetingminutes.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(minutes_file)

minutes_first_page = pdf_reader.getPage(0)
pdf_watermark_reader = PyPDF2.PdfFileReader(open('watermark.pdf', 'rb'))

minutes_first_page.mergePage(pdf_watermark_reader.getPage(0))
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(minutes_first_page)
for page_num in range(1, pdf_reader.numPages):
    page_obj = pdf_reader.getPage(page_num)
    pdf_writer.addPage(page_obj)

result_pdf_file = open('watermarkedCover.pdf', 'wb')
pdf_writer.write(result_pdf_file)
minutes_file.close()
result_pdf_file.close()
