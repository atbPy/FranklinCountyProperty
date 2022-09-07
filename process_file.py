import csv
from datetime import datetime
from database import database_helper


def open_and_read_file(download_file, file_date, current_date):
    with open(download_file, newline='') as csv_file:
        # Move to Row 2 to ignore the headers
        next(csv_file)
        conveyances = csv.reader(csv_file, delimiter=',', quotechar='"')
        record_count = 0

        for row in conveyances:
            record_count += 1

            # Adds a record for each Conveyance Record
            conveyance_record_key = row[0]
            conveyance_record = {"conveyance_number": conveyance_record_key,
                                 "sale_date": datetime.strptime(row[2], '%Y-%m-%d'),
                                 "sale_amount": row[3],
                                 "sale_type": row[4],
                                 "parcel_count": row[5],
                                 "exempt": row[6],
                                 "owner_name_1": row[7],
                                 "owner_name_2": row[8],
                                 "owner_address_1": row[9],
                                 "owner_address_2": row[10]
                                 }

            # If the record already exists, then just update the fields instead of inserting
            if (database_helper.execute_select_query("conveyances", "conveyance_number", conveyance_record_key)) == 0:
                database_helper.insert_record("conveyances", conveyance_record)
            else:
                # Remove the key from the dictionary, since it is not used in update
                conveyance_record.pop("conveyance_number")
                database_helper.update_record("conveyances",
                                              f"'conveyances.conveyance_number'='{conveyance_record_key}'",
                                              conveyance_record)

            # Make sure the Land Use Code (LUC) is in the database.
            land_use_code_key = row[11]
            # File presents 000 as 0, so need to fix
            if land_use_code_key == "0":
                land_use_code_key = "000"
            land_use_code = {"land_use_code": land_use_code_key,
                             "description": "To be determined",
                             "active": True
                             }

            # If the record already exists, then just update the fields instead of inserting
            if (database_helper.execute_select_query("land_use_codes", "land_use_code", land_use_code_key)) == 0:
                database_helper.insert_record("land_use_codes", land_use_code)
            else:
                # Remove the key from the dictionary, since it is not used in update
                land_use_code.pop("land_use_code")
                database_helper.update_record("land_use_codes",
                                              f"'land_use_codes.land_use_code'='{land_use_code_key}'",
                                              land_use_code)

            # Add a record for Conveyance and Parcel Number combination
            conveyance_parcel_key = row[0] + "|" + row[1]
            conveyance_parcel_record = {"conveyance_parcel": conveyance_parcel_key,
                                        "conveyance_number_id": row[0],
                                        "parcel_number": row[1],
                                        "conveyance_date": datetime.strptime(row[2], '%Y-%m-%d'),
                                        "LUC": land_use_code_key,
                                        "site_address": row[12]
                                        }

            # If the record already exists, then just update the fields instead of inserting
            if (database_helper.execute_select_query("conveyance_parcels", "conveyance_parcel", conveyance_parcel_key)) == 0:
                database_helper.insert_record("conveyance_parcels", conveyance_parcel_record)
            else:
                # Remove the key from the dictionary, since it is not used in update
                conveyance_parcel_record.pop("conveyance_parcel")
                database_helper.update_record("conveyance_parcels",
                                              f"'conveyance_parcels.conveyance_parcel'='{conveyance_parcel_key}'",
                                              conveyance_parcel_record)

        # Add a record for when a conveyance file was processed in event there are updates
        conveyance_date_record = {"conveyance_date": file_date,
                                  "processed": True,
                                  "processed_date": current_date,
                                  "records_processed": record_count,
                                  }

        # If the record already exists, then just update the fields instead of inserting
        if (database_helper.execute_select_query("conveyance_dates", "conveyance_date", file_date)) == 0:
            database_helper.insert_record("conveyance_dates", conveyance_date_record)
        else:
            # Remove the key from the dictionary, since it is not used in update
            conveyance_date_record.pop("conveyance_date")
            database_helper.update_record("conveyance_dates", f"'conveyance_dates.conveyance_date'='{file_date}'",
                                          conveyance_date_record)

    #database_helper.print_all_data("conveyances")
    #database_helper.print_all_data("land_use_codes")
    #database_helper.print_all_data("conveyance_parcels")
    #database_helper.print_all_data("conveyance_dates")
    csv_file.close()
