"""Identifies url into document or webpage."""
# pylint: disable=W0312
from converttopdf import ConvertTopdf
from scrape import DoScraping

class Identify():
	"""Identifies the url type as pdf, ppt, pptx, odp, doc, docx, xls, xlsx."""
	def __init__(self, url, pdf):
		"""initiates url, routes for pdf."""
		self.url = url
		self.pdf = pdf
		self.type = 'html'
		self.filename = url
	def classify_url(self):
		"""classifies url."""
		# get filename and type of url
		filename = ""
		filename = self.url.split('/')[-1]
		typeoffile = filename.split('.')[-1]
		rindex = filename.rfind('.')
		filename = filename[0:rindex]
		print(typeoffile)
		if typeoffile in ['txt', 'pdf', 'ppt', 'pptx', 'odp', 'doc', 'docx', 'xls', 'xlsx']:
			#call pdf converter
			return ConvertTopdf(self.url, typeoffile, self.pdf, filename).process()
		#check for google drive and onedrive
		#call web scraper
		return DoScraping(self.url).process()
	