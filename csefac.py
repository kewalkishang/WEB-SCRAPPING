import requests
from bs4 import BeautifulSoup

r=requests.get("http://dayanandasagar.edu/dsce/index.php/about")
soup=BeautifulSoup(r.content)
#print(soup.prettify())
#links=soup.find_all("a")



g_data=soup.find_all("ul",{"class":"cs-fac"})

for item in g_data:
 try:
      print(item.text)
      #print(item.contents[3]) for the 3rd entry in the list
 except:
      pass    
 
 print(" ")
