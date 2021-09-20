# Mission to Mars
### Purpose of Project
I built a web application that scrapes various websites for information related to the Mission to Mars and then displays the information in a single HTML page. 

### Scraping
I utilized a Jupyter Notebook, BeautifulSoup, Pandsas, and Requests/Splinter to complete my initial scraping.

##### Nasa Mars News
I scraped the mars news site to collect the latest news title and paragrpah text.

#### JPL Mars Space Images
I scraped the the featured space image site to pull the current full site featured image.

#### Mars Facts
I utilized Pandas to scrape the table containing facts about Mars from the mars facts webpage

#### Mars Hemispheres
I scraped the site astrogeology to obtain high resolution images for each of Mar's hemispheres along with their titles.

### MongoDB and Flask Application
I utilized MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the various sites.
