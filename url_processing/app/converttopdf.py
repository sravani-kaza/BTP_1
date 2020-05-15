"""Docx to pdf converter."""
# pylint: disable=W0312
import os
import re
import json
import requests
import textract
from fpdf import FPDF


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
				text = response.text
				return json.dumps({'text':text, 'filename':self.filename, 'type':'html'})
			with open(self.path+self.filename+'.'+self.type, 'wb') as file:
				for chunk in response.iter_content():
					if chunk: # filter out keep-alive new chunks
						file.write(chunk)
				file.close()
		except:
			print('file cannot be opened')
			return json.dumps({'error':'Not able to open the file'})
		#convert to pdf if not pdf
		if self.type not in ["pdf"]:
			text = ""
			text = textract.process(self.path+self.filename+'.'+self.type)
			try:
				self.writetopdf(text)
			except:
				print('file cannot be extracted')
				return json.dumps({'error':'file cannot be extracted'})
			# request to pdf parser
		file = self.filename+'.pdf'
		file_path = self.path+self.filename+'.'+'pdf'
		file_data = {'file': open(file_path, 'rb')}
		# print(file_path, file_data)
		# upload path, file
		response = requests.post(self.pdf['pdf_upload'], files=file_data)
		if response.status_code != 200:
			print("ERROR in post request response to pdf")
			return json.dumps({'error':'Error from pdf_parser'})
		# does pdf parsing
		try:
			parser_file_path = "./PDFs/" + file
			dict_json = {}
			dict_json['pdfs'] = [parser_file_path]
			response = requests.post(self.pdf['pdf_parser'], json=json.dumps(dict_json))
			if response.status_code != 200:
				print("ERROR in post request response to pdf")
				return json.dumps({'error':'Error from pdf_parser'})
			text = json.loads(response.text)
			return json.dumps({'text':text, 'type':'html', 'filename':self.filename})
		except:
			print("ERROR in post request response to pdf")
			return json.dumps({'error':'Error from pdf_parser'})
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
			print('pdf cannot be written')
			return None
