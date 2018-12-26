from splinter import Browser
from bs4 import BeautifulSoup

executable_path = {"executable_path": "/Users/sharonsu/Downloads/chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)

def scrape():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)

    news_url = "https://mars.nasa.gov/news/"
    browser.visit(news_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    news_title = soup.find("div", "content_title", "a").text
    news_p = soup.find("div", "rollover_description_inner").text
    output = [news_title, news_p]
    return output

    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    image = soup.find("img", class_="thumb")["src"]
    featured_image_url = "https://www.jpl.nasa.gov" + image
    return featured_image_url

    mars_twitter = "https://twitter.com/marswxreport?lang=en"
    browser.visit(mars_twitter)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    mars_weather = soup.find('div', class_='js-tweet-text-container').text
    return mars_weather

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    facts_url = "https://space-facts.com/mars/"
    browser.visit(facts_url)
    mars_data = pd.read_html(facts_url)
    mars_data = pd.DataFrame(mars_data[0])
    mars_facts = mars_data.to_html(header = False, index = False)
    return mars_facts

    hemispheres_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemispheres_url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    hemisphere_image_urls = []

    products = soup.find("div", class_ = "result-list" )
    hemispheres = soup.find_all("div", class_="item")

    for hemisphere in hemispheres:
        title = hemisphere.find("h3").text
        title = title.replace("Enhanced", "")
        end_link = hemisphere.find("a")["href"]
        image_link = "https://astrogeology.usgs.gov/" + end_link    
        browser.visit(image_link)
        html = browser.html
        soup=BeautifulSoup(html, "html.parser")
        downloads = soup.find("div", class_="downloads")
        image_url = soup.find("a")["href"]
        hemisphere_image_urls.append({"title": title, "img_url": image_url})
    return hemisphere_image_urls