import re
import xlsxwriter

# Removes usless text Arc exports
remove = ['GEORGIA', 'REPORT', 'SYSTEM', '005', 'FROZEN', 'SKU#',
          '<-----------UNITS----------->', 'STORE','CLASS','BATCH', '<-------------UNITS------------->']

# Removes '-' from the top and bottom of each page
regex = "-{20,}"

# Opens the file Arc spits out
with open("QSYSPRT.txt", encoding='latin1') as arcinventory, open("diffoutput.txt", "w") as output:
    for line in arcinventory:
        if not any(remove in line for remove in remove) and line.rstrip():
            if re.match(regex, line):
                continue
            output.write(line)
arcinventory.close()

workbook = xlsxwriter.Workbook('Diff.xlsx')
worksheet = workbook.add_worksheet('kms')

headings = ['Store', 'SKU', 'Description',
            'Frozen Unit(s)', 'Counted Unit(s)', 'Over Unit(s)', 'Short Unit(s)',
            'Frozen Dollar', 'Counted Dollar', 'Over Dollar', 'Short Dollar']

con = 0
for header in headings:
    worksheet.write(1, con, header)
    con += 1
worksheet.set_row(0, 20)

with open("diffoutput.txt", encoding='latin1') as difference:
    row = 2
    for pain in difference:
        hurt = pain.split()
        if len(hurt) == 12:
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
        elif len(hurt) == 13:
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
        elif len(hurt) == 14:
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
        elif len(hurt) == 15:
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
        elif len(hurt) == 16:
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
        elif len(hurt) == 17:
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)
            hurt[2] = hurt[2] + ' ' + hurt.pop(3)

        col = 0
        for data in hurt:
            worksheet.write(row, col, data)
            col += 1
        row += 1

worksheet.set_column('A:K', 15)
worksheet.set_column('C:C', 20)





workbook.close()