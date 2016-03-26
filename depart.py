import requests
from bs4 import BeautifulSoup

r=requests.get("http://dayanandasagar.edu/dsce")
soup=BeautifulSoup(r.content)

d_data=soup.find_all("div",{"class":"widget"})

for item in d_data:
  try:
     print(item.text)
  except:
      pass    
  print(" ")
 
