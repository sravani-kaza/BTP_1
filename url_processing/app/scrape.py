"""WebScraper."""
# pylint: disable=W0312
# import os
# import requests
import re
import json
from urllib.request import urlopen
import urllib.error
# from itertools import product
# from copy import copy
from bs4 import BeautifulSoup
from bs4.element import Comment
from convertdocxpdf import ConvertTopdf

HEADERS = ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]
KILL = ["script", "style", "footer", "symbol", "img", "meta", "[document]", "nav", "input"]
TEXT = ["p"]
def type_url(response):
		"""Categorises url into pdf, webpage, docx.:Arg response => json response of url on request."""
		content_type = response.headers.get('content-type')
		ext = ''
		if 'application/pdf' in content_type:
	 		ext = 'pdf'
		elif 'text/html' in content_type:
	 		ext = 'html'
		# elif 'application/msword' in content_type:
		# 		ext = 'doc'
		elif 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' in content_type:
			ext = 'docx'
		elif ' application/vnd.ms-excel' in content_type:
			ext = 'xls'
		elif 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' in content_type:
			ext = 'xlsx'
		elif 'application/vnd.ms-powerpoint' or 'application/x-powerpoint' in content_type:
			ext = 'ppt'
		elif 'application/vnd.openxmlformats-officedocument.presentationml.presentation' in content_type:
			ext = 'pptx'
		else:
			ext = None
		return ext
# def table_to_2d(table_tag):
# 	"""Converts a given tabe to 2d lists."""
# 	rowspans = []
# 	# track pending rowspans
# 	rows = table_tag.find_all('tr')

# 	# first scan, see how many columns we need
# 	colcount = 0
# 	for rowno, row in enumerate(rows):
# 	    cells = row.find_all(['td', 'th'], recursive=False)
# 	    # count columns (including spanned).
# 	    # add active rowspans from preceding rows
# 	    # we *ignore* the colspan value on the last cell, to prevent
# 	    # creating 'phantom' columns with no actual cells, only extended
# 	    # colspans. This is achieved by hardcoding the last cell width as 1.
# 	    # a colspan of 0 means “fill until the end” but can really only apply
# 	    # to the last cell; ignore it elsewhere.
# 	    colcount = max(
# 	        colcount,
# 	        sum(int(c.get('colspan', 1)) or 1 for c in cells[:-1]) + len(cells[-1:]) + len(rowspans))
# 	    # update rowspan bookkeeping; 0 is a span to the bottom.
# 	    rowspans += [int(c.get('rowspan', 1)) or len(rows) - rowno for c in cells]
# 	    rowspans = [s - 1 for s in rowspans if s > 1]

# 	# it doesn't matter if there are still rowspan numbers 'active'; no extra
# 	# rows to show in the table means the larger than 1 rowspan numbers in the
# 	# last table row are ignored.

# 	# build an empty matrix for all possible cells
# 	table = [[None] * colcount for row in rows]

# 	# fill matrix from row data
# 	rowspans = {}  # track pending rowspans, column number mapping to count
# 	for row, row_elem in enumerate(rows):
# 		span_offset = 0  # how many columns are skipped due to row and colspans
# 		for col, cell in enumerate(row_elem.find_all(['td', 'th'], recursive=False)):
# 	        # adjust for preceding row and colspans
# 			col += span_offset
# 			while rowspans.get(col, 0):
# 				span_offset += 1
# 				col += 1

# 	        # fill table data
# 			rowspan = rowspans[col] = int(cell.get('rowspan', 1)) or len(rows) - row
# 			colspan = int(cell.get('colspan', 1)) or colcount - col
# 			# next column is offset by the colspan
# 			span_offset += colspan - 1
# 			value = cell.get_text()
# 			for drow, dcol in product(range(rowspan), range(colspan)):
# 				try:
# 					table[row + drow][col + dcol] = value
# 					rowspans[col + dcol] = rowspan
# 				except IndexError:
# 	                # rowspan or colspan outside the confines of the table
# 					print("ERROR in parsing tables")
# 					return None
# 		# update rowspan bookkeeping
# 		rowspans = {c: s - 1 for c, s in rowspans.items() if s > 1}
# 	return table
class DoScraping():

	"""Does Web scraping for HTML Pages.urls: url to be summarised."""

	def __init__(self, url, pdf):
		"""Initialises."""
		self.url = url
		self.data = {}
		self.text = ""
		# self.headings = []
		# self.tables = []
		# self.xml = []
		self.pdf = pdf
	def classify_url(self):
		"""Checks the url and classifies the url."""
		#check if url exists
		try:
			ret = urlopen(self.url)
		except urllib.error.HTTPError as error:
			print("ERROR:", error.__dict__)
			# return None
		except urllib.error.URLError as error:
			print("ERROR:", error.__dict__)
			# return None
		urltype = type_url(ret)
		final = {}
		if urltype == 'html':
			result = self.process()
			if result is not None:
				final['text'] = result['text']
				# final['headings'] = result['headings']
				# final['tables'] = result['tables']
				final['type'] = 'html'
				return json.dumps(final)
			return json.dumps({"error":"Error in processing URL"})
		if urltype is None:
			return json.dumps({'error':'URL Rejected : Unknow Type document'})
		if urltype in ["pdf", "doc", "docx", "xls", "xlsx", "pptx", "odt", "txt"]:
			#convert all to pdf
			final['type'] = 'html'
			response_pdf = ConvertTopdf(self.url, urltype, self.pdf).process()
			if response_pdf is None:
				return json.dumps({"error":"Input url file cannot be processed"})
			final['text'] = response_pdf['pdfs'][0]
			return json.dumps(final)
		return json.dumps({"error":"URL is not accepted"})
	def process(self):
		"""Processes the url to text."""
		try:
			html = urlopen(self.url)
		except urllib.error.HTTPError as error:
			print("ERROR:", error.__dict__)
			return None
		except urllib.error.URLError as error:
			print("ERROR:", error.__dict__)
			return None
		text_html = html.read()
		soup = BeautifulSoup(text_html, 'html.parser')
		# self.data['xml'] = copy(soup)
		# kill all script and style elements
		for script in soup(KILL):
		    script.extract()
		# #extract headings,tables
		# for node in soup.find_all(HEADERS+["table"]):
		# 	if node.name in HEADERS:
		# 		self.headings.append(node.text.strip())
		# 	elif node.name == "table":
		# 		eacht = {}
		# 		body = []
		# 		rows = node.find_all('tr')
		# 		caption = node.find_all('caption')
		# 		if len(caption) != 0:
		# 			caption = [x.text.strip() for x in caption]
		# 		else:
		# 			caption = ''
		# 		header = []
		# 		for row in rows:
		# 			head = row.find_all('th')
		# 			if len(head) != 0:
		# 				header += [x.text.strip() for x in head]
		# 				# print(head)
		# 			cols = row.find_all('td')
		# 			cols = [x.text.strip() for x in cols if len(x) != 0]
		# 			if len(cols) != 0:
		# 				# print(cols)
		# 				body += [cols]
		# 		eacht['header'] = header
		# 		eacht['caption'] = caption
		# 		eacht['body'] = table_to_2d(node)
		# 		self.tables.append([eacht])
		#extract text
		for script in soup(["table", "svg"]):
		    script.extract()
		text = []
		for tag in soup.findAll(TEXT+HEADERS):
			eachtext = re.sub(' +', ' ', str(tag.text.strip()))
			# print(tag)
			if tag.parent.name in TEXT+HEADERS:
				continue
			if isinstance(tag, Comment) or tag.name in ["li"]:
				continue
			if tag.name in ["a", "href", "span"]:
				continue
			if tag.name in ["p"]+HEADERS:
				if len(eachtext) > 0:
					text.append(re.sub('\n+', '.', str(eachtext)))
		self.text = '.'.join(chunk for chunk in text if chunk)
		# print(self.text)
		self.data['text'] = self.text
		# self.data['tables'] = self.tables
		# self.data['headings'] = self.headings
		return self.data
