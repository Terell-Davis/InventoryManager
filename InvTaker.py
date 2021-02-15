# I can not take credit for this, Thanks goes to
# Brian C. Lindner (https://github.com/bclindner)
barcodes = {}

while True:
    barcode = str(input("Scan barcode: "))
    # recognize stop code
    if barcode == "stop": break
    # create key in dict if it does not exist
    if barcode not in barcodes:
        barcodes[barcode] = 0
    # increment counter
    barcodes[barcode] += 1

# open up our file
with open("inventorycount.txt", "a") as outputfile:
    # iterate over barcode dict
    for barcode, count in barcodes.items():
        # write line for each of these
        outputfile.write("UPC: {} Count: {}\n".format(barcode, str(count)))
    # ending the with statement closes and saves the file automatically