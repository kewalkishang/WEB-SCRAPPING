import requests
from bs4 import BeautifulSoup

r=requests.get("http://dayanandasagar.edu/dsce/index.php/cse-faculty")
soup=BeautifulSoup(r.content)
#print(soup.prettify()) print the output in a pretty indented way
#links=soup.find_all("a") print all data in the a tag

#for link in links:
  #  print("<a href='%s'>%s</a>"%(link.get("href"),link.text))

g_data=soup.find_all("div",{"class":"media-body top-sto"})

for item in g_data:
 try:
      print(item.contents[1].text)
 except:
      pass    
 try:
      print(item.contents[3].text)
 except:
      pass
 print(" ")
