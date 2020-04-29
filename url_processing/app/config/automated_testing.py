import nose
# import json
import requests

# Test1 - Empty URL
def test_empty_url():
	dictToSend = {'url':' ','pdf_upload': 'http://pdfparser/pdfupload', 'pdf_parser': 'http://pdfparser/pdftotxt'}
	res = requests.post('http://127.0.0.1:5000/extract_page', json=dictToSend)
	assert res.status_code == 200
	assert 'error' in res.json()

# Test2 - Random URL
def test_random_url():
	dictToSend = {'url':'FGCBWYIEUFJ0WPCNUS','pdf_upload': 'http://pdfparser/pdfupload', 'pdf_parser': 'http://pdfparser/pdftotxt'}
	res = requests.post('http://127.0.0.1:5000/extract_page', json=dictToSend)
	assert res.status_code == 200
	assert 'error' in res.json()

#Test 3  - a webpage
def test_positive_url():
	dictToSend = {'url':'https://www.forbesindia.com/blog/finance/reimagining-wealth-management-for-the-2020s/','pdf_upload': 'http://pdfparser/pdfupload', 'pdf_parser': 'http://pdfparser/pdftotxt'}
	res = requests.post('http://127.0.0.1:5000/extract_page', json=dictToSend)
	assert res.status_code == 200

#Test 4  - a pdf
def test_pdf_url():
	dictToSend = {'url':'https://www.csie.ntu.edu.tw/~hsinmu/courses/_media/dsa_13spring/horowitz_306_311_biconnected.pdf','pdf_upload': 'http://pdfparser/pdfupload', 'pdf_parser': 'http://pdfparser/pdftotxt'}
	res = requests.post('http://127.0.0.1:5000/extract_page', json=dictToSend)
	assert res.status_code == 200

#Test 5  - a docx
def test_docx_url():
	dictToSend = {'url':'http://www.e-iceblue.com/images/test.docx','pdf_upload': 'http://pdfparser/pdfupload', 'pdf_parser': 'http://pdfparser/pdftotxt'}
	res = requests.post('http://127.0.0.1:5000/extract_page', json=dictToSend)
	assert res.status_code == 200

if __name__ == '__main__':
    nose.run()
