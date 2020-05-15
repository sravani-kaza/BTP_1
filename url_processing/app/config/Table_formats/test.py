from itertools import product
from bs4 import BeautifulSoup
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
text_html = " "
file = open('./h.html')
text_html = file.read()
soup = BeautifulSoup(text_html, 'html.parser')
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
