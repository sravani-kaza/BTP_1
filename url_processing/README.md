## Input Processing - URL
This is the code dealing with the input processing of URLs (can be webpages, pdfs, pptx, doc, docx, odt, xls, xlsx, txt), and returns clean text output.

### Setup and Installation
Modules used are given in requirements.txt
 
```bash
pip3 install -r requirements.txt
```
### Usage
Run main.py to host the API.
To make a request to the url processing, follow the instructions below.

```python
import json
import requests

urlmain = "http://10.4.24.5:8004/extract_page"

url = 'https://www.fiserv.com/en/about-fiserv/the-point/2019-trends-digital-strategies-for-the-future-of-wealth-management.html'# The url to be processed

pdf_upload = 'http://10.4.24.5:8003/pdfupload' # url to upload pdf file

pdf_parser = 'http://10.4.24.5:8003/pdftotxt' # url to retreive text from pdf


obj = {'url':url,'pdf_upload':pdf_upload,'pdf_parser':pdf_parser}
result = requests.post(urlmain, json = obj)

result = result.json()
print(result.text)
```
### Storage 
	All Documents are stored in this folder url_processing/app/storage

### Errorfile
	Contains the errorfile.txt with all the leftover content from a scraped webpage