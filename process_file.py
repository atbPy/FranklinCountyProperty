import csv
from database import mydatabase
from datetime import datetime


def open_and_read_file(DOWNLOAD_FILE):
    dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='franklinCountyConveyances.sqlite')
    with open(DOWNLOAD_FILE, newline='') as csvfile:
        next(csvfile)
        conveyances = csv.reader(csvfile, delimiter=',', quotechar='"')

        for row in conveyances:
            print(len(row))
            print(row)
            conveyance_record = {"conveyance_number": row[0],
                                     "sale_date": datetime.strptime(row[2], '%Y-%m-%d'),
                                     "sale_amount": row[3],
                                     "sale_type": row[4],
                                     "parcel_count": row[5],
                                     "exempt": row[6],
                                     "owner_name_1": row[7],
                                     "owner_name_2": row[8],
                                     "owner_address_1": row[9],
                                     "owner_address_2": row[10],
                                     "LUC": row[11],
                                     "site_address": row[12]
                                     }
            print(conveyance_record)
            dbms.insert_conveyance(conveyance_record)

    dbms.print_all_data(mydatabase.CONVEYANCES)
    csvfile.close()
