from bs4 import BeautifulSoup
import urllib.request


page = urllib.request.urlopen('http://stats.nba.com/scores')
soup = BeautifulSoup(page,'html.parser')

mydata = soup.findAll("span")
for ele in mydata:
	print (ele)

