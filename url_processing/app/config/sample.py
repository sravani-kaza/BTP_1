import requests
import json
import time
start = time.time()
# dictToSend = {'url':'https://en.wikipedia.org/wiki/Demographics_of_the_Western_Balkans','pdf_upload': 'http://10.4.24.5:8004/pdfupload', 'pdf_parser': 'http://10.4.24.5:8004/pdftotxt'}
# dictToSend = {'url':'wkjgfhowjbfc vow','pdf_upload': 'http://10.4.24.5:8004/pdfupload', 'pdf_parser': 'http://10.4.24.5:8004/pdftotxt'}
# dictToSend = {'url':'https://www.forbesindia.com/blog/finance/reimagining-wealth-management-for-the-2020s/','pdf_upload': 'http://pdfparse/pdfupload', 'pdf_parser': 'http://pdfparse/pdftotxt'}
# dictToSend = {'url':'https://stackoverflow.com/questions/161738/what-is-the-best-regular-expression-to-check-if-a-string-is-a-valid-url', 'pdf_upload': 'http://10.4.24.5:8004/pdfupload','pdf_parser': 'http://10.4.24.5:8004/pdftotxt'}
# dictToSend = {'url':'https://url.spec.whatwg.org/','pdf_upload': 'http://10.4.24.5:8004/pdfupload', 'pdf_parser': 'http://10.4.24.5:8004/pdftotxt' }
# dictToSend = {'url':'https://www.forbesindia.com/blog/finance/reimagining-wealth-management-for-the-2020s/','pdf_upload': 'http://pdfparser/pdfupload', 'pdf_parser': 'http://pdfparser/pdftotxt'}
# dictToSend = {'url':'https://www.csie.ntu.edu.tw/~hsinmu/courses/_media/dsa_13spring/horowitz_306_311_biconnected.pdf','pdf_upload': 'http://pdfparser/pdfupload', 'pdf_parser': 'http://pdfparser/pdftotxt'}
dictToSend = {'url':'http://www.e-iceblue.com/images/test.docx','pdf_upload': 'http://pdfparser/pdfupload', 'pdf_parser': 'http://pdfparser/pdftotxt'}
# dictToSend = {'url':'https://www.finextra.com/blogposting/18168/how-fintech-is-shaping-assets-and-wealth-management','pdf_upload': 'http://pdfparser/pdfupload', 'pdf_parser': 'http://pdfparser/pdftotxt'}
res = requests.post('http://10.4.24.5:8006/extract_page', json=dictToSend)
# res = requests.post('http://127.0.0.1:5000/extract_page', json=dictToSend)
print(time.time() - start)
print(res)
print(res.text)
