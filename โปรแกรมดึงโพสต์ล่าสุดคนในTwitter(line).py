from selenium import webdriver
from bs4 import BeautifulSoup as soup  #เอาไว้ extract html
import time

driverpath=r'E:\Program\Selenium\chromedriver.exe'

opt = webdriver.ChromeOptions()
opt.add_argument('headless')

driver = webdriver.Chrome(driverpath,options=opt)

def TwitterPost(twitter_name):
	url = 'https://twitter.com/{}'.format(twitter_name) 
	driver.get(url)
	time.sleep(5)
	page_html = driver.page_source 
	data = soup(page_html, 'html.parser')
	posts = data.find_all('span',{'class':'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
	founddot = False
	allpost = []
	for p in posts:
		txt = p.text
		if founddot == True:
			allpost.append(txt)
			founddot = False
		if txt == '·':
			founddot = True
		
	return allpost

from songline import Sendline
token = 'bCSAa54GhjyAmn8F8r90z9UQV0IikzwVowAuBtZEPEj'
messenger = Sendline(token)

checktwitter = ['suisei_hosimati','inugamikorone','elonmusk']

for ct in checktwitter:
	texttoline = ''
	post = TwitterPost(ct)
	print('---------- {} ------------'.format(ct))
	texttoline += '---------- {} ------------\n'.format(ct)
	for p in post:
		print(p)
		texttoline += p + '\n\n' 
		print('=====')
    
	messenger.sendtext(texttoline)

driver.close()
