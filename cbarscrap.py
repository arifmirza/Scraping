#libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests

lst=[]
lst1=[]
lst2=[]
from datetime import date
today=date.today().strftime("%m/%d/%Y") 
daterange = pd.date_range('07/28/2020', today)
for single_date in daterange:
    url="https://www.cbar.az/currency/rates?date=" +str(single_date.strftime("%d/%m/%Y"))
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    #souping
    valyutalar=soup.findAll('div',attrs={'class':'valuta'})
    kodlar=soup.findAll('div',attrs={'class':'kod'} )
    kurslar=soup.findAll('div',attrs={'class':'kurs'} )
#creating dataframe
    for kod in kodlar:
        lst.append(kod.text.upper())
    column_names=['Kod']
    cbar_data=pd.DataFrame(lst,columns=column_names)

    for kurs in kurslar:
        lst1.append(kurs.text)
    cbar_data['Kurs']=pd.DataFrame(lst1)

    for valyuta in valyutalar:
        lst2.append(valyuta.text.encode('utf-8'))
    cbar_data['Valyuta']=pd.DataFrame(lst2)
    cbar_data=cbar_data[['Valyuta','Kod','Kurs']
cbar_data.to_csv('file_name.csv’)