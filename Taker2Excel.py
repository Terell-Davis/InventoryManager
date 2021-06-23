import os
import xlsxwriter

# Create Dics.
barcodes = {}
extra = {}

# Path for inventory files (created using InvTaker.py)
path = "./Inventory/"

files = os.listdir(path)

# Searches for all txt files within the specified directory
for text in files:
    if text.endswith(".txt"):
        with open(path + text) as f:
            lines = f.readlines()
        for line in lines:
            test = line.split()
            upc = test[1]
            qt = test[3]
            if upc not in barcodes:
                barcodes[upc] = qt
            else:
                extra[upc] = qt

# Debug for duplicates
print(extra)

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('InventoryCount.xlsx')
worksheet = workbook.add_worksheet("Inventory Count")
worksheet2 = workbook.add_worksheet("Duplicate UPC - add to count")

# labels
worksheet.write('A1', 'UPC')
worksheet.write('B1', 'Description')
worksheet.write('C1', 'Quantity')

worksheet2.write('A1', 'UPC')
worksheet2.write('B1', 'Description')
worksheet2.write('C1', 'Quantity')

# Takes dict values and writes to xlsx
row = 1
brow = 1
for upc, count in barcodes.items():
    worksheet.write(row, 0, upc)
    worksheet.write(row, 2, count)
    row += 1

for upc, count in extra.items():
    worksheet2.write(brow, 0, upc)
    worksheet2.write(brow, 2, count)
    brow += 1

worksheet.set_column('A:A', 15)
worksheet.set_column('B:B', 30)
worksheet.set_column('C:C', 15)

worksheet2.set_column('A:A', 15)
worksheet2.set_column('B:B', 30)
worksheet2.set_column('C:C', 15)

workbook.close()