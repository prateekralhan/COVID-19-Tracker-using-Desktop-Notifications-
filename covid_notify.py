from plyer import notification
import requests
import urllib3
from bs4 import BeautifulSoup
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def getData(url):
    r=requests.get(url,verify=False)
    return r.text

def notifyme(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon = None,
        timeout=10
    )

if __name__ == "__main__":
    #notifyme("Prateek","Let's stop this Virus together")
    myHTMLData= getData("https://www.mohfw.gov.in/")
    #print(myHTMLData)
    soup=BeautifulSoup(myHTMLData,'html.parser')
    #print(soup.prettify())
    mydatastr=""
    for tr in soup.find('tbody').find_all('tr'):
        mydatastr+=tr.get_text()
    mydatastr =mydatastr[1:]
    states= ['Karnataka','Delhi']
    itemlist = mydatastr.split("\n\n")
    for item in itemlist[0:30]:
        datalist = item.split('\n')
        if datalist[1] in states:
            #print(datalist)
            nTtitle = ' Cases of COVID-19 '
            nText = f"STATE/UT : {datalist[1]} \nTotal : {datalist[2]} \nCured : {datalist[3]} \nDeaths : {datalist[4]}"
            notifyme(nTtitle,nText)
            time.sleep(2)
