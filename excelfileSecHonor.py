import pandas as pd
from openpyxl import load_workbook
existing_workbook = load_workbook('existing_sheet.xlsx')
existing_sheet = existing_workbook['Sheet1']
new_data = pd.read_excel('input_sheet.xlsx')
for index, row in new_data.iterrows():
    name = row['Name']
    points = row['Points']
    existing_row = existing_sheet.find(name)
    if not existing_row:
        new_row = [name, points]
        existing_sheet.append(new_row)
    else:
        row_num = existing_row.row
        existing_sheet.cell(row=row_num, column=2).value += points
existing_workbook.save('existing_sheet.xlsx')
