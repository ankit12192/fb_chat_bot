
#---------------------------
#	Importing Modules
#---------------------------

__author__ = 'Ankit'
import  requests
import requests.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from requests.exceptions import ConnectionError
import getpass
import time

#Will be converting into modules
browser = webdriver.Firefox()
browser.get("https://www.facebook.com/?stype=lo&jlou=AfcQ_86A5ZptlNVbtzPICyBj67QzLyd9gw-mUVLxY3F716_HD8wBHd-SuRBxnS3V2l9lZ0J2pzQxn_5TPw-yGOHyi8SpYNyKTRCssjqrb0jrAw&smuh=29247&lh=Ac9E7omSe5g2BsR_")
def login():

    try:
        m=requests.get("https://www.facebook.com/?stype=lo&jlou=AfcQ_86A5ZptlNVbtzPICyBj67QzLyd9gw-mUVLxY3F716_HD8wBHd-SuRBxnS3V2l9lZ0J2pzQxn_5TPw-yGOHyi8SpYNyKTRCssjqrb0jrAw&smuh=29247&lh=Ac9E7omSe5g2BsR_")
    except Exception as  e:
        print("No net connection ")
        exit()
    #browser.get("https://www.facebook.com/?stype=lo&jlou=AfcQ_86A5ZptlNVbtzPICyBj67QzLyd9gw-mUVLxY3F716_HD8wBHd-SuRBxnS3V2l9lZ0J2pzQxn_5TPw-yGOHyi8SpYNyKTRCssjqrb0jrAw&smuh=29247&lh=Ac9E7omSe5g2BsR_")
    inputElement = browser.find_element_by_name('email')
    #phone =raw_input("Enter Phone number or email - > ")
    inputElement2 = browser.find_element_by_name('pass')
    #password = getpass.getpass()
    inputElement.send_keys("spt12192@gmail.com")
    inputElement2.send_keys("qwer12192")
    inputElement.send_keys(Keys.ENTER)
    start_time = time.time()
    try:
        browser.find_element_by_tag_name('textarea').is_displayed()
        print("Logged in !")
        print("total --- %s seconds --- taken to login " % (int(time.time() - start_time)*100))
    except Exception as e:
        print("Can Not login check email/phone or password !")
        exit(0)

def chat():
    fo = open("log.txt", "w+")
    browser.get("https://www.facebook.com/messages/arun.pvsa")
    k= str(browser.find_element_by_class_name("_2nb").text)
    #print k
    fo.write(k)
    print "Here"
    lines = open('log.txt').readlines()
    lines = lines[:-1]
    lines = lines[:-1]
    open('logref.txt', 'w').writelines(lines[6:-1])
    print "here"
    with open('logref.txt') as f:
        print sum(1 for _ in f)
        


login()
chat()
