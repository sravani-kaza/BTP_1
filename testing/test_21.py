#single url
import os
from os import listdir
from os.path import isfile, join
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

mypath = os.getcwd()+'/testing_pdfs/'
onlyfiles = [mypath+f for f in listdir(mypath) if isfile(join(mypath, f))]

#load urls
mypath = os.getcwd() + '/urls_input.txt'
f = open(mypath,"r").read()
urls = f.split('\n')


# load firefox and irel site
driver = webdriver.Firefox()
driver.get("https://irel.iiit.ac.in/digitalee/ui/")
#wait for loading
driver.implicitly_wait(10)

assert 'WMS' in driver.title
assert 'No results found.' not in driver.page_source


email_id = "sravani.kaza@students.iiit.ac.in"


#-----------------------------Single URL Summary Cached-------------------------

#single url upload
upload_url = driver.find_element_by_id("url_list")
upload_button = driver.find_element_by_xpath("//button[contains(text(),'Add')]")
upload_url.send_keys(urls[0])
upload_button.click()


# click select persona
driver.find_element_by_id('select_persona').click()

select_persona = Select(driver.find_element_by_id('select_persona_options'))
select_persona.select_by_value('HNI-AP')

#click summarise
driver.find_element_by_xpath("//button[contains(text(),'Summarise')]").click()

driver.implicitly_wait(600)

assert "No results found." not in driver.page_source

#click on show long form summary
driver.find_element_by_xpath("//button[contains(text(),'Show Long Form Summary')]").click()



#come back to home page
driver.find_element_by_xpath("//button[contains(text(),'Home')]").click()

#---------------------------Single url ML Summary Cached-------------------------



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


#clear all files
driver.find_element_by_xpath("//button[contains(text(),'Clear All Uploaded Files')]").click()

driver.quit()