"""Docx to pdf converter."""
# pylint: disable=W0312
import os
import re
import json
import requests
import textract
from fpdf import FPDF
from pdfhandler import Pdfhandler

LOG_ENABLE = os.environ["DEPLOYED"] if "DEPLOYED" in os.environ else ''
if LOG_ENABLE == "1":
    from logger import Logger
    LOG = Logger(os.getenv('LOGGER_ADDR'))

class ConvertTopdf():

	"""Converts files to pdf."""
	def __init__(self, url, typeoffile, pdf, filename):
		"""Initialises pdf conversion."""
		self.url = url
		self.type = typeoffile
		self.pdf = pdf
		self.filename = filename
		self.path = os.path.dirname(os.path.abspath(__file__))+'/storage/'
	def process(self):
		"""Processes url of documents."""
		#download file
		try:
			print(self.type)
			response = requests.get(self.url, stream=True)
			if self.type == "txt":
				text = response.text.split("\n")
				final = ""
				for line in text:
					if line:
						final += line
				return json.dumps({'text':final, 'filename':self.filename+'.txt', 'type':'html'})
			with open(self.path+self.filename+'.'+self.type, 'wb') as file:
				for chunk in response.iter_content():
					if chunk: # filter out keep-alive new chunks
						file.write(chunk)
				file.close()
		except:
			if LOG_ENABLE == "1":
				LOG.info('url_processing', 'POST', 'NULL', 'NULL', 'file cannot be opened')
			print('file cannot be opened')
			return json.dumps({'error':'Not able to open the file'})
		#convert to pdf if not pdf
		if self.type not in ["pdf"]:
			text = ""
			text = textract.process(self.path+self.filename+'.'+self.type)
			try:
				self.writetopdf(text)
			except:
				if LOG_ENABLE == "1":
					LOG.info('url_processing', 'POST', 'NULL', 'NULL', 'file cannot be opened')
				print('file cannot be extracted')
				return json.dumps({'error':'file cannot be extracted'})
		#pdf handler
		return Pdfhandler(self.filename, self.path, self.pdf).processpdf()

	def writetopdf(self, text):
		"""Write text to pdf."""
		try:
			# save FPDF() class into a
			# variable pdf
			pdf = FPDF('P', 'mm', 'A4')
			pdf.set_auto_page_break(True, 5)
			# Add a page
			pdf.add_page()
			#set font
			pdf.set_font('Arial')
			text = re.sub("\n+", "\n", text.decode())
			pdf.multi_cell(0, 5, text)
			pdf.ln()
			pdf.output(self.path+self.filename+'.'+'pdf')
			return "success"
		except:# MyError as error:
			if LOG_ENABLE == "1":
				LOG.info('url_processing', 'POST', 'NULL', 'NULL', 'pdf cannot be saved')
			print('pdf cannot be written')
			return None
