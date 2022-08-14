import requests

def download_file(DOWNLOAD_FILE, DOWNLOAD_URL):
    r = requests.get(DOWNLOAD_URL, allow_redirects=True)
    open(DOWNLOAD_FILE, 'wb').write(r.content)