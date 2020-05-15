import requests
import time
# import json
start = time.time()
pdf_upload = 'http://10.4.https://en.wikipedia.org/wiki/Table_(information)24.5:32834/pdfupload'
pdf_parser = 'http://10.4.24.5:32834/pdftotxt'
# dictToSend = {'url':'https://en.wikipedia.org/wiki/Demographics_of_the_Western_Balkans','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
# dictToSend = {'url':'wkjgfhowjbfc vow','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
# dictToSend = {'url':'http://25.io/toau/audio/sample.txt','pdf_upload': pdf_upload, 'pdf_parser': pdf_parser}
# dictToSend = {'url':'https://en.wikipedia.org/wiki/Table_(information)','pdf_upload': pdf_upload, 'pdf_parser': pdf_parser}
# dictToSend = {'url':'https://www.csie.ntu.edu.tw/~hsinmu/courses/_media/dsa_13spring/horowitz_306_311_biconnected.pdf','pdf_upload': pdf_upload, 'pdf_parser': pdf_parser}
# dictToSend = {'url':'http://www.e-iceblue.com/images/test.docx','pdf_upload': pdf_upload, 'pdf_parser': pdf_parser}
# dictToSend = {'url':'https://www.fiserv.com/en/about-fiserv/the-point/2019-trends-digital-strategies-for-the-future-of-wealth-management.html','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
# dictToSend = {'url':'https://www.ezesoft.com/insights/blog/trends-were-watching-investment-management-2019','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
dictToSend = {'url':'https://www.investopedia.com/terms/w/wealthmanagement.asp','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
# dictToSend = {'url':'https://www.cnbctv18.com/market/the-two-big-themes-for-the-indian-wealth-management-industry-4021171.htm','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
# dictToSend = {'url':'https://www.financial-planning.com/list/20-wealth-management-trends-for-financial-advisors-in-2020','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
# dictToSend = {'url':'https://en.wikipedia.org/wiki/Asset_management','pdf_upload': 'http://pdfparser/pdfupload', 'pdf_parser': 'http://pdfparser/pdftotxt'}
# dictToSend = {'url':'https://www.thebalance.com/asset-management-companies-for-beginners-4048203','pdf_upload': 'http://pdfparser/pdfupload', 'pdf_parser': 'http://pdfparser/pdftotxt'}
# dictToSend = {'url':'https://www.investopedia.com/terms/p/property-management.asp','pdf_upload': 'http://10.4.24.5:8003/pdfupload', 'pdf_parser': 'http://10.4.24.5:8003/pdftotxt'}
# dictToSend = {'url':'https://certaintyadvicegroup.com/the-3-core-components-of-true-wealth-management/','pdf_upload':pdf_upload, 'pdf_parser':pdf_parser}
# dictToSend = {'url':'http://wilsonporter.com/news/business-solutions-news-and-advice/5-common-components-of-wealth-management/','pdf_upload':pdf_upload,'pdf_parser':pdf_parser}
# res = requests.post('http://10.4.24.5:8004/extract_page', json=dictToSend)
res = requests.post('http://127.0.0.1:5000/extract_page', json=dictToSend)
print(res.json()['text'])
# print(time.time()-start)