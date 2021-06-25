import xlsxwriter
from datetime import date

count = 0
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('Inventory.xlsx')
worksheet = workbook.add_worksheet('Store Inv.')
worksheet2 = workbook.add_worksheet(date.today().strftime("%m-%d-%Y"))

# Heading for excel files
title = ['Description', 'UPC', 'Store', 'Retail On Hand', 'On Hand', 'Class', 'Dept', 'Div', 'Cost On Hand',
         'Current Cost', 'Retail Each', 'Vendor']

next = 0
for label in title:
    worksheet.write(0, next, label)
    next += 1
worksheet.set_row(0, 20)

row = 1
col = 1

# Opens output file from ArcImport.py and writes to excel file
with open("output.txt", encoding='latin1') as inventory:
    for line in inventory:
        count += 1
        if not count % 2 == 0:
            print(line.strip())
            worksheet.write(row, 0, line.strip())
            worksheet.set_row(row, 20)

        if count % 2 == 0:
            test = line.split()
            col2 = 1
            for words in test:
                worksheet.write(row - 1, col2, words)
                col2 += 1
            print(test)
        row += 1
        col += 1

# Set Dimensions
worksheet.set_column('A:A', 30)
worksheet.set_column('B:B', 15)
worksheet.set_column('D:D', 15)
worksheet.set_column('I:K', 15)

workbook.close()