"""Handles pdf."""
# pylint: disable=W0312
import os
import json
import requests

LOG_ENABLE = os.environ["DEPLOYED"] if "DEPLOYED" in os.environ else ''
if LOG_ENABLE == "1":
    from logger import Logger
    LOG = Logger(os.getenv('LOGGER_ADDR'))


class Pdfhandler():

	"""Sends request to pdf module"""
	def __init__(self, filename, path, pdf):
		"""Initialises"""
		self.filename = filename
		self.path = path
		self.pdf = pdf
	def processpdf(self):
		"""request to pdf parser"""
		# request to pdf parser
		file = self.filename+'.pdf'
		file_path = self.path+self.filename+'.'+'pdf'
		file_data = {'file': open(file_path, 'rb')}
		# print(file_path, file_data)
		# upload path, file
		response = requests.post(self.pdf['pdf_upload'], files=file_data)
		if response.status_code != 200:
			if LOG_ENABLE == "1":
				LOG.info('url_processing', 'POST', 'NULL', 'NULL', 'Error from pdf parser')
			print("ERROR in post request response to pdf")
			return json.dumps({'error':'Error from pdf_parser'})
		# does pdf parsing
		try:
			parser_file_path = "./PDFs/" + file
			dict_json = {}
			dict_json['pdfs'] = [parser_file_path]
			response = requests.post(self.pdf['pdf_parser'], json=json.dumps(dict_json))
			if response.status_code != 200:
				if LOG_ENABLE == "1":
					LOG.info('url_processing', 'POST', 'NULL', 'NULL', 'Error from pdf parser')
				print("ERROR in post request response to pdf")
				return json.dumps({'error':'Error from pdf_parser'})
			text = json.loads(response.text)['pdfs'][0]
			return json.dumps({'text':text, 'type':'html', 'filename':self.filename+'.pdf'})
		except:
			if LOG_ENABLE == "1":
				LOG.info('url_processing', 'POST', 'NULL', 'NULL', 'Error from pdf parser')
			print("ERROR in post request response to pdf")
			return json.dumps({'error':'Error from pdf_parser'})
