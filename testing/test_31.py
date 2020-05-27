"""tests pdfs and urls together"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

#load files to test
import os
from os import listdir
from os.path import isfile, join
mypath = os.getcwd()+'/testing_pdfs/'
onlyfiles = [mypath+f for f in listdir(mypath) if isfile(join(mypath, f))]
onlyfiles = onlyfiles[0:2]

#load urls
mypath = os.getcwd() + '/urls_input.txt'
f = open(mypath,"r").read()
urls = f.split('\n')
urls = urls[0:1]

# load firefox and irel site
driver = webdriver.Firefox()
driver.get("https://irel.iiit.ac.in/digitalee/ui/")
#wait for loading
driver.implicitly_wait(10)

assert 'WMS' in driver.title
assert 'No results found.' not in driver.page_source


email_id = "sravani.kaza@students.iiit.ac.in"

#-------------------urls and pdfs Summary cached---------------------------

#upload pdfs
upload_pdf = driver.find_element_by_id("upload_list")
for file in onlyfiles:
	upload_pdf.send_keys(file)

#upload urls

upload_url = driver.find_element_by_id("url_list")
upload_button = driver.find_element_by_xpath("//button[contains(text(),'Add')]")
for url in urls:
	upload_url.send_keys(url)
	upload_button.click()

# click select persona
driver.find_element_by_id('select_persona').click()

select_persona = Select(driver.find_element_by_id('select_persona_options'))
select_persona.select_by_value('HNI-AP')

#click summarise
driver.find_element_by_xpath("//button[contains(text(),'Summarise')]").click()

driver.implicitly_wait(600)
# print(driver.find_element_by_id('ShortForm'))
assert "No results found." not in driver.page_source

#click on show long form summary
driver.find_element_by_xpath("//button[contains(text(),'Show Long Form Summary')]").click()


#come back to home page
driver.find_element_by_xpath("//button[contains(text(),'Home')]").click()
# driver.implicitly_wait(10)
#------------------------------pdfs and urls Multifile Summary cached--------------------


# click select persona
driver.find_element_by_id('select_persona').click()

select_persona = Select(driver.find_element_by_id('select_persona_options'))
select_persona.select_by_value('HNI-AP')

# summarise all files together
if len(urls)+len(onlyfiles) > 1:
	driver.find_element_by_id('multifile_summary_checkbox').click()

#click summarise
driver.find_element_by_xpath("//button[contains(text(),'Summarise')]").click()

driver.implicitly_wait(600)
# print(driver.find_element_by_id('ShortForm'))
assert "No results found." not in driver.page_source



#click on show long form summary
driver.find_element_by_xpath("//button[contains(text(),'Show Long Form Summary')]").click()


#come back to home page
driver.find_element_by_xpath("//button[contains(text(),'Home')]").click()


#-----------------urls and pdfs ML Summary cached-------------------------------------------------


# click select persona
driver.find_element_by_id('select_persona').click()

select_persona = Select(driver.find_element_by_id('select_persona_options'))
select_persona.select_by_value('HNI-AP')

# click ml summary
driver.find_element_by_id('experimental_summariser_checkbox').click()

#click summarise
driver.find_element_by_xpath("//button[contains(text(),'Summarise')]").click()

driver.implicitly_wait(600)
# print(driver.find_element_by_id('ShortForm'))
assert "No results found." not in driver.page_source



#click on show long form summary
driver.find_element_by_xpath("//button[contains(text(),'Show Long Form Summary')]").click()


#come back to home page
driver.find_element_by_xpath("//button[contains(text(),'Home')]").click()

#-------------------------Urls and pdfs Ml summary and multifile cached----------------------------------------------


# click select persona
driver.find_element_by_id('select_persona').click()

select_persona = Select(driver.find_element_by_id('select_persona_options'))
select_persona.select_by_value('HNI-AP')

# summarise all files together
if len(urls)+len(onlyfiles) > 1:
	driver.find_element_by_id('multifile_summary_checkbox').click()

# click ml summary
driver.find_element_by_id('experimental_summariser_checkbox').click()

#click summarise
driver.find_element_by_xpath("//button[contains(text(),'Summarise')]").click()

driver.implicitly_wait(600)
# print(driver.find_element_by_id('ShortForm'))
assert "No results found." not in driver.page_source



#click on show long form summary
driver.find_element_by_xpath("//button[contains(text(),'Show Long Form Summary')]").click()



#come back to home page
driver.find_element_by_xpath("//button[contains(text(),'Home')]").click()

#clear all files
driver.find_element_by_xpath("//button[contains(text(),'Clear All Uploaded Files')]").click()

driver.quit()