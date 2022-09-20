from datetime import date, timedelta
from download_file import download_file
import process_file
import twitter


# def daterange(start_date, end_date):
#     for n in range(int((end_date - start_date).days)):
#         yield start_date + timedelta(n)


# start_date = date(2017, 5, 15)
# end_date = date(2018, 1, 1)
# for current_date in daterange(start_date, end_date):
#     print(current_date.strftime("%Y-%m-%d"))
#     URL_DATE = current_date.strftime("%m/%d/%Y")
#     FILE_DATE = current_date.strftime("%Y-%m-%d")
#
#     # Download URL example https://audr-apps.franklincountyohio.gov/DailyConveyance/Home/DownloadCsv?StartDate=08/12/2022
#     DOWNLOAD_URL = f"https://audr-apps.franklincountyohio.gov/DailyConveyance/Home/DownloadCsv?StartDate={URL_DATE}"
#     DOWNLOAD_FILE = f"downloads/Conveyances-{FILE_DATE}.csv"
#
#     download_file(DOWNLOAD_FILE, DOWNLOAD_URL)
#
#     process_file.open_and_read_file(DOWNLOAD_FILE, FILE_DATE, current_date)



current_date = date.today()
#current_date = date(2022, 9, 18)
URL_DATE = current_date.strftime("%m/%d/%Y")
FILE_DATE = current_date.strftime("%Y-%m-%d")

# Download URL example https://audr-apps.franklincountyohio.gov/DailyConveyance/Home/DownloadCsv?StartDate=08/12/2022
DOWNLOAD_URL = f"https://audr-apps.franklincountyohio.gov/DailyConveyance/Home/DownloadCsv?StartDate={URL_DATE}"
DOWNLOAD_FILE = f"downloads/Conveyances-{FILE_DATE}.csv"

# Manual Test
# DOWNLOAD_URL = f"https://audr-apps.franklincountyohio.gov/DailyConveyance/Home/DownloadCsv?StartDate=08/12/2022"
# DOWNLOAD_FILE = "downloads/Conveyances-2022-08-12.csv"

download_file(DOWNLOAD_FILE, DOWNLOAD_URL)

process_file.open_and_read_file(DOWNLOAD_FILE, FILE_DATE, current_date)

twitter.run_queries(current_date)
