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

eancount = {}
extraean = {}

zero = {}

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
                    if upc in extraean:
                        extraean[upc] = int(extraean.get(upc)) + int(qt)
                    elif upc not in extraean:
                        extraean[upc] = int(qt)
                    print("Updated Quantity")
            else:
                if upc not in upccounts:
                    upccounts[upc] = int(qt)
                elif upc in upccounts:
                    upccounts[upc] = (int(upccounts.get(upc)) + int(qt))
                    print("Updated Quantity")
                    if upc in extra:
                        extra[upc] = int(extra.get(upc)) + int(qt)
                        print("Updated Quantity")
                    elif upc not in extra:
                        extra[upc] = int(qt)
                    else:
                        print("you missed something")

# Debug for duplicates
# print(extraean)
# print(extra)
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('InventoryCount.xlsx')
worksheet = workbook.add_worksheet("Inventory Count")
worksheet2 = workbook.add_worksheet("Inventory Count (Extra)")
worksheet3 = workbook.add_worksheet("Inventory Count (EAN)")
worksheet4 = workbook.add_worksheet("Inventory Count (EAN - Extra)")
worksheet5 = workbook.add_worksheet("Zero")

# labels
worksheet.write('A1', 'UPC')
worksheet.write('B1', 'FinalCount')

worksheet2.write('A1', 'UPC')
worksheet2.write('B1', 'ExtraCount')

worksheet3.write('A1', 'EAN')
worksheet3.write('B1', 'FinalCount')

worksheet4.write('A1', 'EAN')
worksheet4.write('B1', 'ExtraCount')

worksheet5.write('A1', 'UPC')
worksheet5.write('B1', 'Mistakes')


# Takes dict values and writes to xlsx
row = 1
for upc, count in upccounts.items():
    if int(count) == 0:
        zero[upc] = count
        print("Zero Quantity")
    else:
        worksheet.write(row, 0, upc)
        worksheet.write(row, 1, count)
        row += 1

drow = 1
for xupc, xcount in extra.items():
    worksheet2.write(drow, 0, xupc)
    worksheet2.write(drow, 1, xcount)
    drow += 1

brow = 1
for ean, ecount in eancount.items():
    if int(ecount) == 0:
        zero[ean] = ecount
        print("Zero Quantity")
    else:
        worksheet3.write(brow, 0, ean)
        worksheet3.write(brow, 1, ecount)
        brow += 1

crow = 1
for xean, xecount in extraean.items():
    worksheet4.write(crow, 0, xean)
    worksheet4.write(crow, 1, xecount)
    crow += 1

erow = 1
for zupc, zcount in zero.items():
    worksheet5.write(erow, 0, zupc)
    worksheet5.write(erow, 1, zcount)
    erow += 1


worksheet.set_column('A:A', 15)
worksheet.set_column('B:B', 15)

worksheet2.set_column('A:A', 15)
worksheet2.set_column('B:B', 15)

worksheet3.set_column('A:A', 15)
worksheet3.set_column('B:B', 15)

worksheet4.set_column('A:A', 15)
worksheet4.set_column('B:B', 15)

worksheet5.set_column('A:A', 15)
worksheet5.set_column('B:B', 15)

workbook.close()
