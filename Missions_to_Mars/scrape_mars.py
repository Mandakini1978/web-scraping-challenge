from splinter import Browser
from bs4 import BeautifulSoup 
import time
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request 
import os
import pandas as pd
import pymongo

def scrape():
    
    filepath = os.path.join("News - Mars Exploration Program.html")
    with open(filepath, encoding='utf-8') as file:
        html = file.read()

    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find('section',class_='image_and_description_container')

    dates = soup.find_all('div',class_ ='list_date')
    # A blank list to hold dates
    date_list = []
    # Loop over div elements
    for date in dates:
         date_list.append(date.text)

    content_titles = soup.find_all('div',class_ ='content_title')
    # A blank list to hold dates
    content_titles_list = []
    # Loop over div elements
    for title in content_titles:
         content_titles_list.append(title.text)

    articles_body = soup.find_all('div',class_ ='article_teaser_body')
    # A blank list to hold dates
    articles_body_list = []
    # Loop over div elements
    for article in articles_body:
         articles_body_list.append(article.text)

    news_title=content_titles_list[0]
    news_p = articles_body_list[0] 

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://spaceimages-mars.com/"
    browser.visit(url)

    xpath = '//div//a//button[@class="btn btn-outline-light"]'
    
    results = browser.find_by_xpath(xpath)
    button = results[0]
    button.click()

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url = soup.find("img", class_="fancybox-image")["src"]
    featured_image_url= url + img_url
    browser.quit() 

    url_panda = "https://galaxyfacts-mars.com/"
    tables = pd.read_html(url_panda)
    df = tables[0]
    df.columns = ['Description','Mars','Earth']
    mars_facts_list = df.values.tolist()

    #hemisphere
     
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    url = "https://marshemispheres.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    links = soup.find_all('a', class_='itemLink product-item')
    print(links)
    title_list = []
    
    for link in links:
        if (link.h3):
           if (link.h3.text):
            # Append the td to the list
            title_list.append(link.h3.text)
     
  #  title_list_final = []

 #   for i in range (0 , 4) :
  #        title_list_final.append(title_list[i])
  #  print(title_list_final)
    
    links = soup.find_all('div', class_='item')
    img_url_list = []
    url_list = []

    for link in links :
        url=link.find('a')['href']
    #final_url = "https://marshemispheres.com/" + url
    url_list.append(url)
    
    links = soup.find_all('div', class_='item')
    img_url_list = []
    url_list = []

    for link in links :
       url=link.find('a')['href']
       url_list.append(url)
     

    img_url_list = []
    xpath = '//a[@href=' + '"' + url_list[0] + '"' + ']/img'
    results = browser.find_by_xpath(xpath)
    image = results[0]
    image.click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url1 = soup.find("img", class_="wide-image")["src"]
    #img_url1= url + img_url1

    url = "https://marshemispheres.com/"
    browser.visit(url)

    xpath = '//a[@href=' + '"' + url_list[1] + '"' + ']/img'
    results = browser.find_by_xpath(xpath)
    image = results[0]
    image.click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url2 = soup.find("img", class_="wide-image")["src"]
    #img_url2= url + img_url2

    url = "https://marshemispheres.com/"
    browser.visit(url)

    xpath = '//a[@href=' + '"' + url_list[2] + '"' + ']/img'
    results = browser.find_by_xpath(xpath)
    image = results[0]
    image.click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url3 = soup.find("img", class_="wide-image")["src"]
    #img_url3= url + img_url3

    url = "https://marshemispheres.com/"
    browser.visit(url)

    xpath = '//a[@href=' + '"' + url_list[3] + '"' + ']/img'
    results = browser.find_by_xpath(xpath)
    image = results[0]
    image.click()
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img_url4 = soup.find("img", class_="wide-image")["src"]
    #img_url4= url + img_url4

    hemisphere_image_urls = [
    {"title": title_list[0], "img_url": img_url1},
    {"title": title_list[1], "img_url": img_url2},
    {"title": title_list[2], "img_url": img_url3},
    {"title": title_list[3], "img_url": img_url4},
]
   # print(img_url1)
   # print(img_url2)
   # print(img_url3)
   # print(img_url4)
    
    # Store Mars data in a dictionary
    Mars_data = {
        "mars_img": featured_image_url,
        "latest_news_title": news_title,
        "latest_news": news_p,
        "mars_facts": mars_facts_list,
        "Cerberus_title" : title_list[0],"Cerberus_url" : "https://marshemispheres.com/" + img_url1,
        "Schiaparelli_title": title_list[1],"Schiaparelli_url":"https://marshemispheres.com/" + img_url2,
        "Syrtis_Major_title":title_list[2],"Syrtis_Major_url":"https://marshemispheres.com/" + img_url3,
        "Valles_Marineris":title_list[3],"Valles_Marineris_url":"https://marshemispheres.com/"+ img_url4
     }
   
    browser.quit()
    # Return results
    return Mars_data
        
    
