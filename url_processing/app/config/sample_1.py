# Data types
# file_path: path to the pdf file to be extracted
# routes['pdf_upload']: The route to call to send the file across to pdf parser container (the route will be sent in the initial url request)
# routes['pdf_upload']: The route to call to extract the text from the pdf (the route will be sent in the initial url request)
# text: the text that you have send back to the django just like you would have sent it was a html url
import requests
import json
file_path = './../storage/test.pdf'
file_data = {'file': open(file_path,'rb')}

response = requests.post('http://10.4.24.5:8004/pdfupload', files=file_data)
print(response)
file = 'test.pdf'
parser_file_path = "./PDFs/" + file
dict_json = {}
dict_json['pdfs'] = [parser_file_path]

response = requests.post('http://10.4.24.5:8004/pdftotxt', json=json.dumps(dict_json))

text = json.loads(response.text)
print(text)