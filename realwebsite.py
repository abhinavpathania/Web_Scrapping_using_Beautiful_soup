from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=python&txtLocation=').text
soup= BeautifulSoup(html_text,'lxml')
jobs=soup.find_all('li',class_="clearfix job-bx wht-shd-bx")
for job in jobs:
    wewant=job.find('span',class_='sim-posted').span.text
    if (wewant=='Posted few days ago'):
        company=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
        skills=job.find('span',class_='srp-skills').text.replace(' ','')
        Link=job.header.h2.a['href']
        print(f"Company: {company}") 
        print(f"Skills: {skills}")
        print(f"Quick Link: {Link}")
        print()
    else:
        exit 
