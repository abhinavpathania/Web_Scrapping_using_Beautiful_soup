from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content=html_file.read()
    
    # Create a BeautifulSoup object and specify the parser
    soup=BeautifulSoup(content,'lxml')
    
    # Find the first h1 tag in the HTML document
    tags=soup.find("h1")
    print(tags.text)
    course_cards=soup.find_all("div",class_="card")
    for course in course_cards:
        prices=course.a.text.split()[-1]
        print (prices)
    
    

    
