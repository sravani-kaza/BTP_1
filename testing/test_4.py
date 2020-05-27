"""tests add personna, reset personna"""
import os
import time
from os import listdir
from os.path import isfile, join
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# load firefox and irel site
driver = webdriver.Firefox()
driver.get("https://irel.iiit.ac.in/digitalee/ui/")
#wait for loading
driver.implicitly_wait(60)

assert 'WMS' in driver.title
assert 'No results found.' not in driver.page_source


#------------------- Add Personna------------------------------------------

#click on add persona button
driver.find_element_by_id("add_persona").click()

new_personna_name = 'wealth'
new_key_words = 'wealth, property, investment'
driver.find_element_by_id("add_persona_new_persona").send_keys(new_personna_name)
driver.find_element_by_id("add_persona_keywords").send_keys(new_key_words)
driver.find_element_by_xpath("//button[@value='Add Persona']").click()
driver.implicitly_wait(60)

#check added personna
#click select persona
driver.find_element_by_id('select_persona').click()

select_persona = Select(driver.find_element_by_id('select_persona_options'))
select_persona.select_by_value(new_personna_name)