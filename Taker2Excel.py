import xlsxwriter

count = 0
# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('InventoryCount.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'UPC')
worksheet.write('B1', 'Description')
worksheet.write('C1', 'Quantity')





worksheet.set_column('A:A', 15)
worksheet.set_column('B:B', 30)
worksheet.set_column('C:C', 15)