#! python3
# readCensusExcel.py

import openpyxl, pprint

print('workbook opening...')
wb = openpyxl.load_workbook('/tmp/censuspopdata.xlsx')

# readCensusExcel.py:8: DeprecationWarning: Call to deprecated function get_sheet_by_name (Use wb[sheetname]).
sheet = wb['Population by Census Tract']
county_data = {}

print('read row data...')
for row in range(2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value


    county_data.setdefault(state, {})
    county_data[state].setdefault(county, {'tracts':0, 'pop': 0})

    county_data[state][county]['tracts'] += 1
    county_data[state][county]['pop'] += int(pop)

print('writhing...')

result_file = open('/tmp/census2010.py', 'w')
result_file.write('all_data = ' + pprint.pformat(county_data))
result_file.close()

print('finish')

