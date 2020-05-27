### Automated Test Scripts using Selenium and Python


### Setup and Installation
Modules used are given in requirements.txt
 
```bash
pip3 install -r requirements.txt
```
### Usage
Run main.py to run the tests

### Covered Test Cases

### File          Input					Tested Features

	test_1	=>	Single pdfs             Normal , ML Summary
										Short, Long Form Summaries
										Download
										Email
										Home Button

	test_2	=>	Single Urls             Normal , ML Summary
										Short, Long Form Summaries
										Download
										Email
										Home Button

	test_3	=>	Multiple Urls, pdfs		Normal, ML Summary
										Short, Long Form Summaries
										Single, all files together
										Email
										Download
										Home Button

	test_11	=>	Single pdfs             Normal , ML Summary
										Short, Long Form Summaries
										Caching
										Clear Button
										Home Button

	test_21	=>	Single Urls             Normal , ML Summary
										Short, Long Form Summaries
										Caching
										Clear Button
										Home Button

	test_31	=>	Multiple Urls, pdfs		Normal, ML Summary
										Short, Long Form Summaries
										Single, All files together
										Caching
										Clear Button
										Home Button

	test_4	=>	Added new persona		Add persona
										reset persona


### If all the above work well, u get 8 downloads and 8 emails