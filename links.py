from bs4 import BeautifulSoup
import requests
url="http://www.utexas.edu/world/univ/alpha/"
page = requests.get(url)
soup = BeautifulSoup(page.content)
universities=soup.find_all('a',class_='institution')
for university in universities:
    print(university['href']+","+university.string)
