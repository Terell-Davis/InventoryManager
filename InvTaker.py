barcodes = {}
section = str(input("Enter name of Section: "))

while True:
    barcode = str(input("Scan barcode: "))
    # recognize stop code
    if barcode == "stop": break

    if barcode.startswith("-"):
        print("Removed")
        barcodes[barcode[1:]] -= 1

    if barcode not in barcodes and not barcode.startswith("-"):
        barcodes[barcode] = 0

    if not barcode.startswith("-"):
        barcodes[barcode] += 1

with open(section + ".txt", "a") as outputfile:
    # iterate over barcode dict
    for barcode, count in barcodes.items():
        # write line for each of these
        outputfile.write("UPC: {} Count: {}\n".format(barcode, str(count)))