#! python3

import openpyxl
import setup

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active

sheet.freeze_panes = 'A2' # or None
wb.save('produceSales_freezePane.xlsx')
