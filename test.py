from random import random
import requests
from selenium import webdriver
import time
import ddddocr
import datetime

ocr = ddddocr.DdddOcr()

login_url = "https://cas.hrbeu.edu.cn/cas/login?service=http%3A%2F%2Frgyy.hrbeu.edu.cn%2Fcas%2Findex.php%3Fcallback%3Dhttp%3A%2F%2Frgyy.hrbeu.edu.cn%2Fhome%2Fbook%2Fmore%2Flib%2F12%2Ftype%2F4%2Fday%2F#/"
bro = webdriver.Chrome(executable_path='./chromedriver.exe')

html_data = requests.get(login_url)


bro.get(login_url)

# login_url = "https://cas.hrbeu.edu.cn/cas/login?service=http%3A%2F%2Frgyy.hrbeu.edu.cn%2Fcas%2Findex.php%3Fcallback%3Dhttp%3A%2F%2Frgyy.hrbeu.edu.cn%2Fhome%2Fbook%2Fmore%2Flib%2F12%2Ftype%2F4%2Fday%2F#/"

captcha_img = bro.find_element_by_xpath('//img[@alt="验证码。"]')

img = captcha_img.screenshot_as_png
res = ocr.classification(img)
#模拟自动登录
username_tag = bro.find_element_by_id("username")
passwd_tag = bro.find_element_by_id("password")
captcha_tag = bro.find_element_by_id("captcha")
print

#输入自己的学号/密码
studentId = "XXXXXX"
password = "XXXXXX"
username_tag.send_keys(studentId)
passwd_tag.send_keys(password)
captcha_tag.send_keys(res)
#time.sleep(3)
buttn = bro.find_element_by_id('login-submit')
buttn.click()
time.sleep(2)

#获取明天日期
def getTom():
    today =  datetime.datetime.today()
    tomorrow = today + datetime.timedelta(days=1)
    tmp = str(tomorrow)
    tom = tmp.split(" ")[0]
    return tom

#获得明天日期

tomDate = getTom()
bookurl = "http://rgyy.hrbeu.edu.cn/home/book/more/lib/12/type/4/day/"
BookUrl = bookurl + tomDate

#如果有名额就会自动抢完//要是没有我也没啥办法
bro.get(BookUrl)
bookButton = bro.find_element_by_xpath('//span[@class="btn btn-info"]')
time.sleep(1)
bookButton.click()

checkFull = bro.find_element_by_xpath('/html/body/div[4]/div[1]/div[3]/button[1]')
checkAva = bro.find_element_by_xpath('//div[@class="col-xs-12 col-md-3 visible-xs visible-sm images"]/button[@class="btn btn-success signUp"]')
time.sleep(2)

if checkAva is not None and checkFull is None:
    WannaBookButton = checkAva
    WannaBookButton.click()
    phoneTag = bro.find_element_by_xpath('//input[@name="mobile"]')
    #第一次预约完电话会绑定好就不用输入了
    # phoneNumber = "XXXXXXX"
    # phoneTag.send_keys(phoneNumber)
    okButton = bro.find_element_by_xpath('//button[@i-id="ok"]')
    okButton.click()

elif checkFull is not None: 
    print("暂无名额捏期待下一轮名额")

    #可以每隔多久重复一次

time.sleep(10)
bro.quit()