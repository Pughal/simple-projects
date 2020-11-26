from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    content = html_file.read()
    # print(content)
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())
    #h3_tags = soup.find_all('h3')
    #print(h3_tags)
    #for course in h3_tags:
        #print(course.text)
    
    course_cards = soup.find_all('div', class_= 'container' )
    for course in course_cards:
        #print(course.h1)
        #course_name = course.h1.text
        course_link = course.a
        #print(course_name)
        print(course_link)

