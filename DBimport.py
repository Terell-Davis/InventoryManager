import mysql.connector
from getpass import getpass

mydb = mysql.connector.connect(
        host="localhost",
        user="root", # input("Username: "),
        password=getpass("Password: "),
        database="onhandupc",
)

sku = "NULL"; desc = "NULL"; cost = 00.00; retail = 00.00; avail = 0
iclass = 800; dept = 800; store = 000; vendor = "NULL"; val = {};

cursor = mydb.cursor()

count = 0
with open("output.txt", encoding='latin1') as input:
    for line in input:
        count += 1
        if not count % 2 == 0:
            desc = line.strip()

        if count % 2 == 0:
            test = line.split()

            try:
                val = {
                    "sku": test[0],
                    "desc": desc,
                    "cost": test[8],
                    "retail": test[9],
                    "available": test[3],
                    "class": test[4],
                    "dept": test[5],
                    "store": test[1],
                    "vendor": test[10]
                }
            except IndexError:
                val = {
                    "sku": test[0],
                    "desc": desc,
                    "cost": 'null',
                    "retail": 'null',
                    "available": test[3],
                    "class": test[4],
                    "dept": test[5],
                    "store": test[1],
                    "vendor": 'null'
                }

        sql = "INSERT INTO onhandupc.item(sku, `desc`, cost, retail, available, class, dept, store, vendor) " \
              f'VALUES({val["sku"]}, "{val["desc"]}", {val["cost"]}, {val["retail"]}, {val["available"]}, {val["class"]}, {val["dept"]}, {val["store"]}, "{val["vendor"]}")'
        print(sql)
        cursor.execute(sql)
mydb.commit()
print(cursor.rowcount, "record inserted.")

