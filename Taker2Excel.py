import os
import xlsxwriter
import openpyxl

# Store onHand Inventory w/ Descriptions
StoreInv = './Inventory.xlsx'
StoreSheet = 'Store Inv.'

wbinv = openpyxl.load_workbook(StoreInv)

InvSheet = wbinv[StoreSheet]

# Create Dics.
upccounts = {}
extra = {}

ogUPC = {}
ogextra = {}

eancount = {}
extraean = {}

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

            # check for EANs cause MBS cant count pass 11
            if len(upc) == 13:
                if upc not in eancount:
                    eancount[upc] = int(qt)
                elif upc in eancount:
                    eancount[upc] = int(eancount.get(upc)) + int(qt)
                    extraean[upc] = qt
                    print("Updated Quantity")

            if len(upc) <= 12:
                if len(upc) == 12:
                    aUPC = str(upc)[:-1]
                    if upc not in ogUPC:
                        ogUPC[upc] = int(qt)
                    elif upc in ogUPC:
                        ogUPC[upc] = int(ogUPC.get(upc)) + int(qt)

                    if aUPC not in upccounts:
                        upccounts[aUPC] = int(qt)
                    elif aUPC in upccounts:
                        upccounts[aUPC] = int(upccounts.get(aUPC)) + int(qt)

                elif len(upc) < 12:
                    if upc not in upccounts:
                        upccounts[upc] = int(qt)
                    elif upc in upccounts:
                        upccounts[upc] = (int(upccounts.get(upc)) + int(qt))

# Debug for duplicates
print(extraean)
print(ogUPC)
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('InventoryCount.xlsx')
worksheet = workbook.add_worksheet("Inventory Count")
worksheet3 = workbook.add_worksheet("Inventory Count (OG UPC)")
worksheet2 = workbook.add_worksheet("Inventory Count (EAN)")
worksheet4 = workbook.add_worksheet("Inventory Count (EAN - Extra)")

# labels
worksheet.write('A1', 'UPC')
worksheet.write('B1', 'Description')
worksheet.write('C1', 'Quantity')
worksheet.write('D1', 'On Hand')

worksheet2.write('A1', 'UPC')
worksheet2.write('B1', 'Description')
worksheet2.write('C1', 'Quantity')
worksheet2.write('D1', 'On Hand')

worksheet3.write('A1', 'UPC')
worksheet3.write('B1', 'Description')
worksheet3.write('C1', 'Quantity')
worksheet3.write('D1', 'On Hand')

worksheet4.write('A1', 'UPC')
worksheet4.write('B1', 'Description')
worksheet4.write('C1', 'Quantity')
worksheet4.write('D1', 'On Hand')

# Takes dict values and writes to xlsx
row = 1
for upc, count in upccounts.items():
    worksheet.write(row, 0, upc)
    worksheet.write(row, 2, count)
    row += 1

arow = 1
for oupc, ocount in ogUPC.items():
    worksheet3.write(arow, 0, oupc)
    worksheet3.write(arow, 2, ocount)
    arow += 1

brow = 1
for ean, ecount in eancount.items():
    worksheet2.write(brow, 0, ean)
    worksheet2.write(brow, 2, ecount)
    brow += 1

crow = 1
for xean, xecount in extraean.items():
    worksheet4.write(crow, 0, xean)
    worksheet4.write(crow, 2, xecount)
    brow += 1



worksheet.set_column('A:A', 15)
worksheet.set_column('B:B', 30)
worksheet.set_column('C:C', 15)

worksheet2.set_column('A:A', 15)
worksheet2.set_column('B:B', 30)
worksheet2.set_column('C:C', 15)

worksheet3.set_column('A:A', 15)
worksheet3.set_column('B:B', 30)
worksheet3.set_column('C:C', 15)

worksheet4.set_column('A:A', 15)
worksheet4.set_column('B:B', 30)
worksheet4.set_column('C:C', 15)

workbook.close()
