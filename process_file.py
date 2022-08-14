import csv

def open_and_read_file(DOWNLOAD_FILE):
    with open(DOWNLOAD_FILE, newline='') as csvfile:
        conveyances = csv.reader(csvfile, delimiter=',', quotechar='"')
        row_count = (len(list(conveyances)))

        if row_count > 1:
            for row in conveyances:
                print(len(row))
                print(row)
        else:
            print("No records available to process")

