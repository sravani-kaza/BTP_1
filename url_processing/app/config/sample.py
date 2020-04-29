import requests
import time
# import json
start = time.time()
# dictToSend = {'url':'https://en.wikipedia.org/wiki/Demographics_of_the_Western_Balkans','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
# dictToSend = {'url':'wkjgfhowjbfc vow','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
# dictToSend = {'url':'http://www.e-iceblue.com/images/test.docx','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
dictToSend = {'url':'https://www.fiserv.com/en/about-fiserv/the-point/2019-trends-digital-strategies-for-the-future-of-wealth-management.html','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
# dictToSend = {'url':'https://www.ezesoft.com/insights/blog/trends-were-watching-investment-management-2019','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
# dictToSend = {'url':'https://www.investopedia.com/terms/w/wealthmanagement.asp','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
#dictToSend = {'url':'https://www.nasdaq.com/articles/topics-framing-the-asset-management-industry-in-2019-and-beyond-2020-01-10','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
# dictToSend = {'url':'https://www.cnbctv18.com/market/the-two-big-themes-for-the-indian-wealth-management-industry-4021171.htm','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
# dictToSend = {'url':'https://www.financial-planning.com/list/20-wealth-management-trends-for-financial-advisors-in-2020','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
#no dictToSend = {'url':'https://en.wikipedia.org/wiki/Asset_management','pdf_upload': 'http://pdfparser/pdfupload', 'pdf_parser': 'http://pdfparser/pdftotxt'}
# dictToSend = {'url':'https://www.thebalance.com/asset-management-companies-for-beginners-4048203','pdf_upload': 'http://pdfparser/pdfupload', 'pdf_parser': 'http://pdfparser/pdftotxt'}
# dictToSend = {'url':'https://www.investopedia.com/terms/p/property-management.asp','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
#no dictToSend = {'url':'https://www.quora.com/What-is-meant-by-wealth-in-economics','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
res = requests.post('http://10.4.24.5:8004/extract_page', json=dictToSend)
# res = requests.post('http://127.0.0.1:5000/extract_page', json=dictToSend)
print(time.time() - start)
print(res.status_code)
print(res.text)
# with open('text') as f:
# 	f.write('{"content":res.text}')
