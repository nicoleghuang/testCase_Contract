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
    #time.sleep(3)
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

    #sell contract
    for i in range(5):
        m=59+i
        n=0.15+i
        browser.implicitly_wait(10)
        browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/span[2]/input').send_keys(m)
        browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/span[2]/input').send_keys(n)
        browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[6]/a').click()
        print 'sold successfully'
    time.sleep(5)

    #equal to minimum quantity
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/span[2]/input').send_keys(
        '19')
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/span[2]/input').send_keys(
        '0.01')
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[6]/a').click()
    time.sleep(5)

    now=time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    #less than minimum quantity
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/span[2]/input').send_keys('66')
    try:
        browser.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/span[2]/input').send_keys('0.001')
    except:
        browser.get_screenshot_as_file('D:\\selenium_use_case\\error_png\\' + now + '.png')
    time.sleep(5)
    #more than residual quantity
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/span[2]/input').clear()
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/span[2]/input').send_keys('99')
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/span[2]/input').clear()
    try:
        browser.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/span[2]/input').send_keys('10000')
    except:
        browser.get_screenshot_as_file('D:\\selenium_use_case\\error_png\\'+now+'.png')
    time.sleep(5)

    #decimal digits of quantity
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/span[2]/input').clear()
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/span[2]/input').send_keys(
        '100')
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/span[2]/input').clear()
    try:
        browser.find_element_by_xpath(
            '/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/span[2]/input').send_keys('0.6666666')
    except:
        browser.get_screenshot_as_file('D:\\selenium_use_case\\error_png\\' + now + '.png')
    time.sleep(5)

    #decimal digits of price
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/span[2]/input').clear()
    try:
        browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/span[2]/input').send_keys('33.33333333')
    except:
        browser.get_screenshot_as_file('D:\\selenium_use_case\\error_png\\' + now + '.png')
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/span[2]/input').clear()
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/span[2]/input').send_keys('0.66')
    browser.find_element_by_xpath('/html/body/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[6]/a').click()

