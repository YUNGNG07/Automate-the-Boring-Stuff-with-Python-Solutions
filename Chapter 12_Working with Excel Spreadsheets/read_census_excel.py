"""
Tabulates population and number of census tracts for each county.
"""

import openpyxl
import pprint

print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
county_data = {}

print('Reading rows...')
for row in range(2, sheet.get_highest_row() + 1):
    # Each row in the spreadsheet has data for one census tract
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    # Make sure the key for state exists
    county_data.setdefault(state, {})
    # Make sure the key for the county exists
    county_data[state].setdefault(county, {'tracts':0, 'pop':0})

    # Each row represents one census tract, so increment by one
    county_data[state][county]['tracts'] += 1
    # Increase the county pop by the pop in this census tract
    county_data[state][county]['pop'] += int(pop)

    # Open a new text file and write the contents of county_data to it
    print('Writing results...')
    result_file = open('census2010.py', 'w')
    result_file.write('allData = ' + pprint.pformat(county_data))
    result_file.close()
    print('Done.')
