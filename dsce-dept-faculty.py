import requests
from bs4 import BeautifulSoup

r=requests.get("http://dayanandasagar.edu/dsce/")
soup=BeautifulSoup(r.content,"html.parser")

print("GET THE FACULTY NAMES FROM DIFFERENT DEPARTMENTS OF DSCE")
asf=soup.find_all("div",{"class":"widget"}) #get all the dept of the college
for asfs in asf:                                                                  
   print(asfs.text)
   
sa=input("Enter the proper dept name-")

links=soup.find_all("a") #print all data in the 'a' tag
for link in links:
   if(link.text==sa):  #get the link to the particular department
     j=requests.get('http://dayanandasagar.edu'+link.get("href"))
     curry=BeautifulSoup(j.content,"html.parser")
      
asd=curry.find_all("div",{"class":"col-sm-3 col-md-3"}) #get all the faculty names
for asds in asd:
     print(asds.text)
   

   
