"""Docx to pdf converter."""
# pylint: disable=W0312
import os
import re
import json
import requests
import textract
from fpdf import FPDF

class MyError(Exception):
	"""Constructor Initialiser."""

	def __init__(self, value):
		"""Initialises."""
		Exception.__init__(self)
		self.value = value

	def __str__(self):
		"""Prints error."""
		(repr(self.value))

def writetopdf(text, name):
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
		pdf.output(name)
		return "success"
	except MyError as error:
		print('A New Exception occured: ', error.value)
		return None

class ConvertTopdf():
	"""Converts files to pdf."""

	def __init__(self, url, typeoffile, pdf):
		"""Initialises pdf conversion."""
		self.url = url
		self.type = typeoffile
		self.pdf = pdf
		# path = str(__file__)
		# rindex = os.path.rfind('/')
		self.path = os.path.dirname(os.path.abspath(__file__))+'/storage/'
	def process(self):
		"""Processes url of word documents."""
		try:
			right = requests.get(self.url, stream=True)
			fname = ""
			fname = self.url.split('/')[-1]
			rindex = fname.rfind('.')
			fname = fname[0:rindex]
			if right.status_code == 200:
			    with open(self.path+fname+'.'+self.type, 'wb') as file:
			    	for chunk in right.iter_content():
			    		if chunk: # filter out keep-alive new chunks
			        		file.write(chunk)
			    file.close()
			if self.type not in ["pdf"]:
				text = textract.process(self.path+fname+'.'+self.type)
				writetopdf(text, self.path+fname+'.'+'pdf')
				self.type = 'pdf'
			file_path = self.path+fname+'.'+'pdf'
			file = fname+'.pdf'
			file_data = {'file': open(file_path, 'rb')}
			# print(file)
			# print(file_path)
			# print(file_data)
			response = requests.post(self.pdf['pdf_upload'], files=file_data)
			# print("hello" ,response.status_code)
			if response.status_code != 200:
				print("ERROR in post request response to pdf")
				return None
			parser_file_path = "./PDFs/" + file
			dict_json = {}
			dict_json['pdfs'] = [parser_file_path]
			# print(file)
			response = requests.post(self.pdf['pdf_parser'], json=json.dumps(dict_json))
			if response.status_code != 200:
				print("ERROR in post request response to pdf")
				return None
			# print("hiii",response.text)
			text = json.loads(response.text)
			# print(text)
			return text
		except MyError as error:
			print('A New Exception occured: ', error.value)
			return None
	def hello(self):
		"""Does Nothing."""
		print("hello", self)
