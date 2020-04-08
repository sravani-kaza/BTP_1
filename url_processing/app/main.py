'''Does url processing'''
# pylint: disable=W0312
from flask import Flask
from flask import request
from scrape import DoScraping


app = Flask(__name__)
@app.route('/extract_page', methods=['POST'])
def processurl():
	'''processes the url as html or pdf
	Arg: data => input json object with url,'''
	data = request.get_json(force=True)
	url = data['url']
	pdf = {'pdf_upload' : data['pdf_upload'], 'pdf_parser' : data['pdf_parser']}
	response = DoScraping(url, pdf).classify_url()
	# print(response)
	return response

@app.route('/')
def hello():
	'''hello world'''
	return "hello world from url_processing"

if __name__ == '__main__':
	app.run(debug=True)#'0.0.0.0',debug=True,port=80)
