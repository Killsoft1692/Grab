# -*- coding: utf-8 -*-

from grab import Grab
import urllib

def find_text(xpath):
	return (g.doc.select(xpath).text())

url = 'http://mysku.ru'
g = Grab()
g.go(url)
for num in g.doc.select('//a[@class="a-link"]'):
	a = num.text()
	if a.isdigit():
		n = a
	else:
		continue
print n
for item in range(1,int(n)+1):
	out_li = url+'/index/page'+str(item)
	print out_li
	g.go(out_li)
	for element in g.doc.select('//div[@class="topic-title"]/a[@href]'):
		# 
		post_link = element.attr('href')
		print post_link
		g.go(post_link)
		print find_text('//h1[@class="topic-title"]')
		print find_text('//li[@class="price"]')
		print find_text('//div[@class="description"]')
		print find_text('//ul[@class="topic-footer"]')
		for img in g.doc.select('//div[@class="description"]/img'):
			img_link = img.attr('src')
			#urllib.urlretrieve(img_link, 'image.jpg') #as example
			print img_link
		#break

		