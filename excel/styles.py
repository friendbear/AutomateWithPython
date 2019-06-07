#! python3

import openpyxl
from openpyxl.styles import Font
import setup

wb = openpyxl.Workbook()

sheet = wb['Sheet']
font_obj = Font(name='Times New Roman', bold=True)

sheet['A1'].font = font_obj
sheet['A1'] = 'Bold Times New Roman'
sheet['B3'].font = Font(size=24, italic=True)
sheet['B3'] = '24 pt Italic'
wb.save('styles.xlsx')
