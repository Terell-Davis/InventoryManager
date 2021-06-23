import re

# Removes usless text Arc exports
remove = ['GEORGIA', 'REPORT', 'SYSTEM', 'RETAIL', '', 'SKU TOTAL', 'SKU STORE', 'SKU                     STORE',
          'STORE TOTAL', 'FINAL TOTAL']

# Removes '-' from the top and bottom of each page
regex = "-{20,}"

# Opens the file Arc spits out
with open("QSYSPRT.txt", encoding='latin1') as arcinventory, open("output.txt", "w") as output:
    for line in arcinventory:
        if not any(remove in line for remove in remove) and line.rstrip():
            if re.match(regex, line):
                continue
            output.write(line)
arcinventory.close()
