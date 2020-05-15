# # from urllib.request import urlopen
# # import urllib.parse
# # from os.path import splitext
# # import requests
# # from fpdf import FPDF
# # import re
# # # url = 'https://iiitaphyd-my.sharepoint.com/:p:/g/personal/sravani_kaza_students_iiit_ac_in/EckmNPLqlupLpkm1hnAa1LYBBt-JdefjIs_EvXuca6UJkg?e=gcPENE&download=1'
# # # url = 'https://docs.google.com/document/d/1RGzQ4jxl3rpO6G   print(response)mGseNW7DtYVeNiR5-U8R937dGM5rI/edit'
# # # file_id = '1RGzQ4jxl3rpO6GmGseNW7DtYVeNiR5-U8R937dGM5rI'
# # url = 'https://drive.google.com/file/d/1IBwyevFQC-ggKiDu8qIFr7T9va7CZhxu/view?usp=sharing'
# # file_id = '1IBwyevFQC-ggKiDu8qIFr7T9va7CZhxu'


# # def download_file_from_google_drive(id, destination):
# #     URL = "https://docs.google.com/uc?export=download"

# #     session = requests.Session()

# #     response = session.get(URL, params = { 'id' : id }, stream = True)
# #     # token = get_confirm_token(response)

# #     # if token:
# #     #     params = { 'id' : id, 'confirm' : token }
# #     #     response = session.get(URL, params = params, stream = True)
# #     print(response.headers)
# #     print(response.content)
# #     # print(response.json())
# #     #writetopdf(response.content,destination)

# # def get_confirm_token(response):
# #     for key, value in response.cookies.items():
# #         if key.startswith('download_warning'):
# #             return value

# #     return None

# # def writetopdf(text, name):
# #     """Write text to pdf."""
# #     # try:
# #     #     # save FPDF() class into a
# #         # variable pdf
# #     pdf = FPDF('P', 'mm', 'A4')
# #     pdf.set_auto_page_break(True, 5)
# #     # Add a page
# #     pdf.add_page()
# #     #set font
# #     pdf.set_font('Arial')
# #     # text = re.sub("\n+", "\n", text)
# #     print(type(text))
# #     pdf.multi_cell(0, 5, text)
# #     pdf.ln()
# #     pdf.output(name)
# #     return "success"
# #     # except:# MyError as error:
# #     #     print('pdf cannot be written')
# #     #     return None

# # destination = './1'
# # import time
# # s = time.time()
# # download_file_from_google_drive(file_id, destination)
# # print(time.time()-s)
# # # import time
# # # s = time.time()
# # # from google_drive_downloader import GoogleDriveDownloader as gdd

# # # gdd.download_file_from_google_drive(file_id='1IBwyevFQC-ggKiDu8qIFr7T9va7CZhxu',
# # #                                     dest_path='./1.zip',
# # #                                     unzip=True)
# # # print(time.time()-s)
import gdown
import os
import time
s = time.time()
url = 'https://drive.google.com/uc?id=1IBwyevFQC-ggKiDu8qIFr7T9va7CZhxu'
url = 'https://iiitaphyd-my.sharepoint.com/:p:/g/personal/sravani_kaza_students_iiit_ac_in/EckmNPLqlupLpkm1hnAa1LYBBt-JdefjIs_EvXuca6UJkg?e=gcPENE&download=1'
os.system('gdown '+url)
print(time.time()-s)

# # from pydrive.auth import GoogleAuth
# # import time
# # s = time.time()
# # gauth = GoogleAuth()
# # gauth.LocalWebserverAuth()
# # drive = GoogleDrive(gauth)
# # file_obj = drive.CreateFile({'id':'1IBwyevFQC-ggKiDu8qIFr7T9va7CZhxu'})
# # file_obj.GetContentFile('Demo.txt') 
# # print(time.time()-s)


# from urllib.request import urlretrieve
# onedriveURL = "https://onedrive.live.com/download?cid=9194394ABFA6631C&resid=9194394ABFA6631C%2127355&authkey=AO6VrIdT_CZ_HU0"
# copy_onedrive = "1.csv"
# urlretrieve(onedriveURL , copy_onedrive)