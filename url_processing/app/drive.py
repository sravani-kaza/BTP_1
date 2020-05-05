from urllib.request import urlopen
import urllib.parse
from os.path import splitext

# url = 'https://iiitaphyd-my.sharepoint.com/:p:/g/personal/sravani_kaza_students_iiit_ac_in/EckmNPLqlupLpkm1hnAa1LYBBt-JdefjIs_EvXuca6UJkg?e=gcPENE&download=1'
# url = 'https://docs.google.com/document/d/1RGzQ4jxl3rpO6G   print(response)mGseNW7DtYVeNiR5-U8R937dGM5rI/edit'
# file_id = '1RGzQ4jxl3rpO6GmGseNW7DtYVeNiR5-U8R937dGM5rI'
url = 'https://drive.google.com/file/d/1IBwyevFQC-ggKiDu8qIFr7T9va7CZhxu/view?usp=sharing'
file_id = '1IBwyevFQC-ggKiDu8qIFr7T9va7CZhxu'
import requests

def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)
    print(response)
    # save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    print(response.content)
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

destination = '/home/1.txt'
download_file_from_google_drive(file_id, destination)