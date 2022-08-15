import csv
from database import mydatabase
from datetime import datetime
from database import database_helper


def open_and_read_file(DOWNLOAD_FILE, FILE_DATE, current_date):
    with open(DOWNLOAD_FILE, newline='') as csvfile:
        # Move to Row 2 to ignore the headers
        next(csvfile)
        conveyances = csv.reader(csvfile, delimiter=',', quotechar='"')
        record_count = 0

        for row in conveyances:
            record_count += 1
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
            database_helper.insert_record("conveyances", conveyance_record)

        conveyance_date_record = {"conveyance_date": FILE_DATE,
                                  "processed": True,
                                  "processed_date": current_date,
                                  "records_processed": record_count
                                  }

        # If the record already exists, then just update the fields instead of inserting
        # Todo: make this a function instead of putting the query in this
        if (database_helper.execute_select_query(f"SELECT * FROM 'conveyance_dates' WHERE 'conveyance_date' = '{FILE_DATE}';")) is None:
            database_helper.insert_record("conveyance_dates", conveyance_date_record)
        else:
            conveyance_date_record = {"processed": True,
                                      "processed_date": current_date,
                                      "records_processed": record_count
                                      }
            database_helper.update_record("conveyance_dates", conveyance_date_record)



    database_helper.print_all_data("conveyances")
    database_helper.print_all_data("conveyance_dates")
    csvfile.close()
