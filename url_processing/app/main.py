"""Does url processing."""
# pylint: disable=W0312
import os
from flask import Flask
from flask import request
from identifyurl import Identify

# check if logger is enabled
LOG_ENABLE = os.environ["DEPLOYED"] if "DEPLOYED" in os.environ else ''

if LOG_ENABLE == "1":
    from logger import Logger
    LOG = Logger(os.getenv('LOGGER_ADDR'))


app = Flask(__name__)
@app.route('/extract_page', methods=['POST'])
def processurl():
	"""Processes the url as html or pdf.Arg: data => input json object with url."""
	data = request.get_json(force=True)
	# print(data)
	url = data['url']
	# pdf has the routes to pdf parser
	pdf = {'pdf_upload' : data['pdf_upload'], 'pdf_parser' : data['pdf_parser']}
	# print('hello')
	if LOG_ENABLE == "1":
		LOG.info('url_processing', 'POST', 'NULL', 'NULL', 'URL processed successfully')
	result = Identify(url, pdf).classify_url()
	return result

@app.route('/')
def hello():
	"""Hello world."""
	return "hello world from url_processing"

if __name__ == '__main__':
	app.run('0.0.0.0', debug=True, port=80)
