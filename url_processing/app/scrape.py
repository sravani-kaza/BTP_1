"""WebScraper."""
# pylint: disable=W0312
import re
import os
import json
from urllib.request import urlopen
import urllib.error
from itertools import product
from bs4 import BeautifulSoup
from bs4.element import Comment
LOG_ENABLE = os.environ["DEPLOYED"] if "DEPLOYED" in os.environ else ''

if LOG_ENABLE == "1":
    from logger import Logger
    LOG = Logger(os.getenv('LOGGER_ADDR'))

HEADERS = ["h1", "h2", "h3", "h4", "h5", "h6", "h7", "h8"]
KILL = ["script", "style", "footer", "symbol", "meta", "[document]", "nav", "input"]
TEXT = ["p", "li", "img"]

#tables commented for now
def table_to_2d(table_tag):
	"""Converts a given table to matrix."""
	rowspans = []
	# track pending rowspans
	rows = table_tag.find_all('tr')
	# first scan, see how many columns we need
	colcount = 0
	for rowno, row in enumerate(rows):
	    cells = row.find_all(['td', 'th'], recursive=False)
	    # count columns (including spanned).
	    colcount = max(
	        colcount,
	        sum(int(c.get('colspan', 1)) or 1 for c in cells[:-1]) + len(cells[-1:]) + len(rowspans))
	    # update rowspan bookkeeping; 0 is a span to the bottom.
	    rowspans += [int(c.get('rowspan', 1)) or len(rows) - rowno for c in cells]
	    rowspans = [s - 1 for s in rowspans if s > 1]
 	# build an empty matrix for all possible cells
	table = [[None] * colcount for row in rows]
	# fill matrix from row data
	rowspans = {}  # track pending rowspans, column number mapping to count
	for row, row_elem in enumerate(rows):
		span_offset = 0  # how many columns are skipped due to row and colspans
		for col, cell in enumerate(row_elem.find_all(['td', 'th'], recursive=False)):
	        # adjust for preceding row and colspans
			col += span_offset
			while rowspans.get(col, 0):
				span_offset += 1
				col += 1
			# fill table data
			rowspan = rowspans[col] = int(cell.get('rowspan', 1)) or len(rows) - row
			colspan = int(cell.get('colspan', 1)) or colcount - col
			# next column is offset by the colspan
			span_offset += colspan - 1
			value = cell.get_text().split('\n')
			final_value = ''
			for text in value:
				final_value += text+" "
			for drow, dcol in product(range(rowspan), range(colspan)):
				try:
					table[row + drow][col + dcol] = final_value
					rowspans[col + dcol] = rowspan
				except IndexError:
	                # rowspan or colspan outside the confines of the table
					print("ERROR in parsing tables")
					return None
		# update rowspan bookkeeping
		rowspans = {c: s - 1 for c, s in rowspans.items() if s > 1}
	return table
class DoScraping():

	"""Does Web scraping for HTML Pages.urls: url to be summarised."""

	def __init__(self, url):
		"""Initialises."""
		print('Initialises')
		self.url = url
		self.data = {}
		self.text = ""
		self.tables = []
	def process(self):
		"""Processes the url to text."""
		try:
			html = urlopen(self.url)
			# print('hello')
		except urllib.error.HTTPError as error:
			print("ERROR:", error.__dict__)
			return json.dumps({"error":"URL is not accepted"})
		except:
			print("ERROR: cannot open url")
			return json.dumps({"error":"URL is not accepted"})
		text_html = html.read()
		soup = BeautifulSoup(text_html, 'html.parser')
		# kill all script and style elements
		for script in soup(KILL):
		    script.extract()
		# #extracttables
		for node in soup.find_all(["table"]):
			if node.name == "table":
				eacht = {}
				body = []
				rows = node.find_all('tr')
				caption = node.find_all('caption')
				if len(caption) != 0:
					caption = [x.text.strip() for x in caption]
				else:
					caption = ''
				header = []
				for row in rows:
					head = row.find_all('th')
					if len(head) != 0:
						header += [x.text.strip() for x in head]
						# print(head)
					cols = row.find_all('td')
					cols = [x.text.strip() for x in cols if len(x) != 0]
					if len(cols) != 0:
						# print(cols)
						body += [cols]
				# eacht['header'] = header
				eacht['caption'] = caption
				eacht['body'] = table_to_2d(node)
				print(eacht)
				self.tables.append([eacht])
		#extract text
		for script in soup(["table", "svg"]):
		    script.extract()
		text = []
		for tag in soup.findAll(TEXT + HEADERS):
			eachtext = re.sub(' +', ' ', str(tag.text.strip()))
			# print(tag)
			#remove comments
			if isinstance(tag, Comment):
				continue
			# if parent tag is processed , child need not be processed again
			if tag.parent.name in TEXT+HEADERS or tag.name in ["li"] or tag.name in ["a", "href", "span"]:
				continue
			if tag.name in TEXT+HEADERS:
				if len(eachtext) > 0:
					final_text = re.sub('\n+', '\n', str(eachtext))
					printable = ""
					for char in final_text:
						if char == '"':
							printable = printable[:-1]
							continue
						if char.isprintable() == 1:
							printable = printable + char
					printable = printable.encode('ascii', errors='ignore').strip().decode('ascii')
					printable = re.sub('\n+', '.', str(printable))
					if len(printable) > 0:
						text.append(re.sub('\n+', '.', str(printable)))
		self.text = '.'.join(chunk for chunk in text if chunk)
		# remove unnecessary punctuation
		text = self.text.split('.')
		self.text = ''
		for line in text:
			if len(line) > 0:
				self.text += line + '.'
		# print(self.text)
		# print("Tables")
		for script in soup(TEXT+HEADERS):
			script.extract()

		# write to error file if not retreived in text
		path = os.path.dirname(os.path.abspath(__file__))+'/errorfile/'
		with open(path+'errorfile.txt', 'w+') as file:
			for line in (soup.get_text()).split("\n"):
				# print(line)
				if line != "\n" and line not in self.text:
					file.write(line+"\n")
			for table in self.tables:
				file.write(str(table)+"\n")
		file.close()
		# write to logger
		if LOG_ENABLE == "1":
			LOG.info('url_processing', 'POST', 'NULL', 'NULL', 'Errorfile written sucessfully')

		self.data['text'] = self.text
		self.data['type'] = 'html'
		self.data['filename'] = self.url
		# self.data['tables'] = self.tables
		# print(self.data)
		return self.data
