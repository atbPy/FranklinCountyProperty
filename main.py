import requests
from datetime import datetime
from download_file import download_file
import process_file

current_date = datetime.now()
URL_DATE = current_date.strftime("%m/%d/%Y")
FILE_DATE = current_date.strftime("%Y-%m-%d")

# Download URL example https://audr-apps.franklincountyohio.gov/DailyConveyance/Home/DownloadCsv?StartDate=08/12/2022
DOWNLOAD_URL = f"https://audr-apps.franklincountyohio.gov/DailyConveyance/Home/DownloadCsv?StartDate={URL_DATE}"
DOWNLOAD_FILE = f"downloads/Conveyances-{FILE_DATE}.csv"

download_file(DOWNLOAD_FILE, DOWNLOAD_URL)

process_file.open_and_read_file(DOWNLOAD_FILE)



