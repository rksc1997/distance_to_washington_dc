# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 16:02:21 2020

@author: Rahul.chauhan
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 13:01:57 2020

@author: Rahul.chauhan
"""


from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import bs4
import urllib
from datetime import timedelta, date
import time
import socket
from pprint import pprint
import pandas as pd
import numpy as np
import re
from urllib.request import urlopen
import requests
from random import shuffle 
from collections import OrderedDict
from datetime import datetime
from time import gmtime, strftime
    
var2=range(1,75)
for j in range(55, len(var2)):
    driver = webdriver.Chrome(executable_path="C://Users//rahul.chauhan//Desktop//Industrial Concentration//Analysis//chromedriver.exe")
    driver.get("https://www.distancecalculator.net/")
    driver.implicitly_wait(15)
    driver.maximize_window()
    df = pd.DataFrame(columns=['distance', 'address', 'cty_fips'])
#df = pd.DataFrame(columns=['part1cd', 'pincode'])
    input_p="C://Users//rahul.chauhan//Desktop//Industrial Concentration//Analysis//state"
    k=str(j)
    suffix=".xlsx"
    new_excel = pd.read_excel(input_p + k + suffix)
    var = list(new_excel['address'])
    var7= list(new_excel['cty_fips'])
#    var3=list(new_excel['part1cd'])
    print(len(var))
    for i in range(0, len(var)):
        address= driver.find_element_by_xpath('//*[@id="distancefrom"]')
        address.send_keys(var[i])
        address1 = driver.find_element_by_xpath('//*[@id="distanceto"]')
        address1.send_keys("Washington D C")
        print(i)
        driver.find_element_by_xpath('//*[@id="hae"]').click()
        driver.implicitly_wait(15)
        
        def check_exists_by_xpath(xpath):
            try:
            #branch = '//*[@id="search-listing"]/div[2]/div/div[1]/div/ul/li[1]'
                driver.find_element_by_xpath(xpath)
            except NoSuchElementException:
                   return False
            return True
        branch_dummy = check_exists_by_xpath('//*[@id="totaldistancekm"]')
        if branch_dummy == True:
            distance = driver.find_element_by_xpath('//*[@id="totaldistancekm"]').text

           
            df = df.append({ 'distance': distance, 'address': var[i], 'cty_fips': var7[i]}, ignore_index=True)
            #df = df.append({'part1cd': var[i], 'pincode': pincode, 'address': address, 'state': state, 'district': district, 'bank_name': bank_name }, ignore_index=True)
            #df.append(data, ignore_index = True)
            #df = df.append({'part1cd': var[i], 'pincode': branch_dummy}, ignore_index=True)

        next_page="https://www.distancecalculator.net/"
        driver.get(next_page)
            
        i=i+1
    
    outp= 'C://Users//rahul.chauhan//Desktop//Industrial Concentration//Analysis//dist'
    suffix_o= '.csv'
    df.to_csv(outp + k + suffix_o)
    driver.close()
j=j+1   
    
