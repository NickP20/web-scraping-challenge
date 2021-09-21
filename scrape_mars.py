from splinter import Browser
from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager

def init_browser():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    mars_info = {}

    # Visit mars news site
    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_='article_teaser_body').text
    mars_info["news_p"]=news_p
    mars_info['news_title']=news_title

    mars_info['featured_image'] = mars_image(browser)
    mars_info['mars_facts'] = mars_facts()
    mars_info['mars_hemispheres'] =mars_hemispheres(browser)

    browser.quit()

    return mars_info

def mars_image(browser):
    img_url = 'https://spaceimages-mars.com/'
    browser.visit(img_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    time.sleep(1)

    image = soup.find('div', class_='floating_text_area')
    link = image.find("a")['href']

    featured_image_url = 'https://spaceimages-mars.com/'+link

    return featured_image_url

def mars_facts():
    url = 'https://galaxyfacts-mars.com/'
    tables = pd.read_html(url)
    mars_df = tables[0]
    mars_df.columns = ['Description', 'Mars', 'Earth']
    mars_df.set_index('Description', inplace=True)
    html_table = mars_df.to_html()
    html_table.replace('\n', '')

    return html_table

def mars_hemispheres(browser):
    hemispheres_url = 'https://marshemispheres.com/'
    browser.visit(hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='item')
    hemisphere_img_urls = []

    for item in items:
        title = item.find('h3').text
        hemisphere_url = 'https://marshemispheres.com/' + item.find('a', class_='itemLink product-item')['href']
        
        browser.visit(hemisphere_url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        hemisphere_img_url = 'https://marshemispheres.com/' + soup.find('img', class_='wide-image')['src']
        hemisphere_img_urls.append({'title': title, 'img_url': hemisphere_img_url})
    return hemisphere_img_urls

if __name__ == "__main__":
    print(init_browser())