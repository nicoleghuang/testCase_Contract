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
    browser.implicitly_wait(5)

    #switch to english version
    #browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[2]/li[3]/a').click()
    #browser.implicitly_wait(3)
    #browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[2]/li[3]/ul/li[2]/a').click()
    #login
    browser.find_element_by_xpath('//*[@id="signin-form"]/div[2]/div/div[2]/div/input').send_keys(k)
    browser.find_element_by_xpath('//*[@id="signin-form"]/div[3]/div/input[2]').send_keys(v)
    time.sleep(15)
    browser.find_element_by_xpath('//*[@id="signin-form"]/a').click()
    browser.implicitly_wait(10)

    #enter contract trading market
    browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[1]/li[2]/a').click()
    browser.implicitly_wait(5)
    browser.find_element_by_xpath('/html/body/div/div[1]/div/ul/li[4]/a').click()
    print 'contract trading market'

    #switch to subAccount
    browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[2]/li[1]/a').click()
    browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[2]/li[1]/ul/li[1]/a').click()
    #browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[2]/li[1]/ul/li[1]/ul/li[2]/a/span').click()
    browser.find_element_by_xpath('//*[@id="navbar-collapse"]/ul[2]/li[1]/ul/li[1]/ul/li[2]/a')


    #buy contract
    browser.implicitly_wait(10)
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[3]/span[2]/input').send_keys('0.8')
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[4]/span[2]/input').send_keys('0.9')
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[6]/a').click()

    # sell contract
    browser.implicitly_wait(10)
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/span[2]/input').send_keys(
        '88')
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/span[2]/input').send_keys(
        '2.9')
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[6]/a').click()

