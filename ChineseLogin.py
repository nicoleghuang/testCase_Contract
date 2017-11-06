#coding=utf-8
from selenium import webdriver
import fun
import os,time
#browser=webdriver.Chrome()
#browser.maximize_window()
#browser.get("http://bibo.viabtc.com:8000/signin/")
#ld=fun.diction()
for k,v in fun.diction().items():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get("http://bibo.viabtc.com:8000/signin/")
    print k,v
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('//*[@id="signin-form"]/div[2]/div/div[2]/div/input').send_keys(k)
    browser.find_element_by_xpath('//*[@id="signin-form"]/div[3]/div/input[2]').send_keys(v)
    time.sleep(15)
    browser.find_element_by_xpath('//*[@id="signin-form"]/a').click()
    browser.implicitly_wait(10)
    #browser.quit()

    browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[1]/li[2]/a').click()
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/div/div[1]/div/ul/li[4]/a').click()
    print 'contract trading market'
    # switch to english version
    browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[2]/li[3]/a').click()
    browser.implicitly_wait(3)
    browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[2]/li[3]/ul/li[2]/a').click()

