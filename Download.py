import requests
import wget
import zipfile
import os

zip_file_path = "C:\Packages\Plugins\Microsoft.CPlat.Core.RunCommandWindows\1.1.9\Downloads\"

# get the latest chrome driver version number
url = 'https://chromedriver.storage.googleapis.com/LATEST_RELEASE'
response = requests.get(url)
version_number = response.text

# build the donwload url
download_url = "https://chromedriver.storage.googleapis.com/" + version_number +"/chromedriver_win32.zip"

# download the zip file using the url built above
latest_driver_zip = wget.download(download_url,'chromedriver.zip')

# extract the zip file
with zipfile.ZipFile(latest_driver_zip, 'r') as zip_ref:
    zip_ref.extractall(zip_file_path) # you can specify the destination folder path here
# delete the zip file downloaded above
# os.remove(latest_driver_zip)