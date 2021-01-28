import re

remove = ['GEORGIA', 'REPORT', 'SYSTEM', 'RETAIL','','SKU TOTAL', 'SKU STORE', 'SKU']
regex = "-{20,}"


with open("QSYSPRT.txt") as input, open("output.txt", "w") as output:
    for line in input:
        if not any(remove in line for remove in remove) and line.rstrip():
            if re.match(regex, line):
                continue
            output.write(line)
input.close()


