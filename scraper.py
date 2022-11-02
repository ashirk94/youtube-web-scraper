from bs4 import BeautifulSoup
#from selenium import webdriver
import requests

html = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/#calling-a-tag-is-like-calling-find-all').text

soup = BeautifulSoup(html, 'lxml')
details = soup.find('a', class_="reference external").text
print(details)