#!/usr/bin/env python
# coding: utf-8

# In[1]:

def scrape():

    from bs4 import BeautifulSoup
    from splinter import Browser
    import requests
    import pandas as pd


    # In[2]:


    executable_path = {'executable_path':'c:\\Users\\medinam\\Downloads\\chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    # # NASA Mars News

    # In[3]:


    article_url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(article_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[4]:


    article = soup.find("div", class_='list_text')
    news_title = article.find("div", class_="content_title").text
    news_p = article.find("div", class_="article_teaser_body").text
    print(news_title)
    print(news_p)


    # # JPL Mars Space Images - Featured Image

    # In[5]:


    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")


    # In[6]:


    image = soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image
    print(featured_image_url)


    # # Mars Facts

    # In[8]:


    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    mars_info = pd.read_html(facts_url)
    mars_info = pd.DataFrame(mars_info[0])
    mars_facts = mars_info.to_html(header = False, index = False)
    print(mars_facts)


    # In[ ]:





    # # Mars Hemispheres

    # In[ ]:


    # hemisphere_image_urls = [
    #     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
    #     {"title": "Cerberus Hemisphere", "img_url": "..."},
    #     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
    #     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
    # ]


# In[ ]:
    dict = {

        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image": featured_image_url,
        "mars_facts": mars_facts
        # "hemisphere_images": hemisphere_image_urls
    }

    return dict




# In[ ]:



