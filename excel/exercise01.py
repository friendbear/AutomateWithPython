import openpyxl
import os, shutil

os.chdir('~/Downloads')

wb = openpyxl.load_workbook('example.xlsx')

for sheet_name in wb.getsheet_names:
    sheet = wb.get_sheet_by_name(sheet_name)
    print(sheet['A1'].value)
    print(sheet.cell(row=1, column=2).value)



