#coding=utf-8
from selenium import webdriver
import fun
import os,time
for k,v in fun.diction().items():
    browser = webdriver.Chrome()
    browser.maximize_window()
    #open website
    browser.get("http://bibo.viabtc.com:8000/signin/")
    print k,v
    #time.sleep(5)
    browser.implicitly_wait(5)

    #switch to english version
    browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[2]/li[3]/a').click()
    #time.sleep(3)
    browser.implicitly_wait(3)
    browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[2]/li[3]/ul/li[2]/a').click()
    #login
    browser.find_element_by_xpath('//*[@id="signin-form"]/div[2]/div/div[2]/div/input').send_keys(k)
    browser.find_element_by_xpath('//*[@id="signin-form"]/div[3]/div/input[2]').send_keys(v)
    time.sleep(15)
    browser.find_element_by_xpath('//*[@id="signin-form"]/a').click()
    #time.sleep(10)
    browser.implicitly_wait(10)

    #enter contract trading market
    browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[1]/li[2]/a').click()
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/div/div[1]/div/ul/li[4]/a').click()
    print 'contract trading market'
    #choose L3
    browser.find_element_by_xpath('/html/body/div/div[2]/div[1]/ul/li[2]/a').click()
    #to deposit
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[2]/a').click()