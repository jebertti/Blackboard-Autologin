import os
import time
from selenium import webdriver
from getpass import getpass

print("Welcome to the Blackboard Autologin program\n")
username = input("Enter your username: \n")
password = input("Enter your password: \n")


#Opens Blackboard and maximizes the window
driver = webdriver.Chrome("C:\\CS Projects\\Autologin\\chromedriver.exe")
driver.get("https://uic.blackboard.com/")
driver.maximize_window()

#Finds and clicks login button
sign_in = driver.find_element_by_id("loginurl")
sign_in.click()
time.sleep(1.0)

#Finds and inputs username
username_textbox = driver.find_element_by_id("UserID")
username_textbox.send_keys(username)
time.sleep(1.0)

#Finds and inputs password
password_textbox = driver.find_element_by_id("password")
password_textbox.send_keys(password)
time.sleep(1.0)

#Logs in
login = driver.find_element_by_id("disable-on-click")
login.submit()
time.sleep(5.0)

my_courses = driver.find_element_by_xpath("//a[contains(@href,'https://uic.blackboard.com/ultra/course')]")
my_courses.click()
time.sleep(2.0)

math_class = driver.find_element_by_xpath('//*[@title="MATH 181 Calculus II (38943) 2021 Spring"]')
math_class.click()
time.sleep(2.0)
