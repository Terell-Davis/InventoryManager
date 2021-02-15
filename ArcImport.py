import re

remove = ['GEORGIA', 'REPORT', 'SYSTEM', 'RETAIL','','SKU TOTAL', 'SKU STORE', 'SKU                     STORE','STORE TOTAL', 'FINAL TOTAL']
regex = "-{20,}"


with open("QSYSPRT.txt",encoding='latin1') as input, open("output.txt", "w") as output:
    for line in input:
        if not any(remove in line for remove in remove) and line.rstrip():
            if re.match(regex, line):
                continue
            output.write(line)
input.close()


