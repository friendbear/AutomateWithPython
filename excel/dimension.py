#! python3

import openpyxl

import setup

wb = openpyxl.Workbook()
sheet = wb.active

sheet['A1'] = 'Tall row'
sheet['B1'] = 'Wide column'

sheet.row_dimensions[1].height = 70
sheet.column_dimensions['B'].width = 20

wb.save('dimentions.xlsx')
