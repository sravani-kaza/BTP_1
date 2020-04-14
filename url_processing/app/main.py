"""Does url processing."""
# pylint: disable=W0312
from flask import Flask
from flask import request
from scrape import DoScraping

import os

LOG_ENABLE = os.environ["DEPLOYED"] if "DEPLOYED" in os.environ else ''

if LOG_ENABLE == "1":
    from logger import Logger
    LOG = Logger(os.getenv('LOGGER_ADDR'))


app = Flask(__name__)
@app.route('/extract_page', methods=['POST'])
def processurl():
	"""Processes the url as html or pdf.Arg: data => input json object with url."""
	data = request.get_json(force=True)
	url = data['url']
	pdf = {'pdf_upload' : data['pdf_upload'], 'pdf_parser' : data['pdf_parser']}
	response = DoScraping(url, pdf).classify_url()
	# print(response)

	if LOG_ENABLE == "1":
		LOG.info('url_processing', 'POST', 'NULL', 'NULL', 'URL processed successfully')

	return response

@app.route('/')
def hello():
	"""Hello world."""
	return "hello world from url_processing"

if __name__ == '__main__':
	app.run(debug=True)#'0.0.0.0',debug=True,port=80)
