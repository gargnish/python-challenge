import time
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
from selenium import webdriver
from threading import Thread as th
import datetime as dt
import pymongo
from bson import ObjectId

conn = 'mongodb://127.0.0.1:27017'
client = pymongo.MongoClient(conn)
db = client.mars


def fx_init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=True)
    return browser


def fx_scrape_news():
    """
    output:
    {'description': 'On May 5, millions of Californians may witness the historic first interplanetary launch from America’s West Coast.',
     'list_date': 'April  6, 2018',
     'title': 'Bound for Mars: Countdown to First Interplanetary Launch from California'}
    """
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser = fx_init_browser()
    browser.visit(url)
    html = browser.html
    time.sleep(1)
    soup = bs(html, "html.parser")
    v_data_dict = {}
    list_text = soup.find_all('div', {'class': 'list_text'})[0]
    v_latest_list_date = list_text.find_all('div', {'class': 'list_date'})[0].get_text()
    v_latest_title = list_text.find_all('a', {'target': '_self'})[0].get_text()
    v_latest_description = list_text.find_all('div', {'class': 'article_teaser_body'})[0].get_text()

    v_data_dict = {"list_date": v_latest_list_date, "title": v_latest_title, "description": v_latest_description}
    global v_scrape_news
    v_scrape_news = v_data_dict
    return v_scrape_news


def fx_scrape_weather():
    """
    output = 
    'Sol 2019 (April 11, 2018), Sunny, high -6C/21F, low -75C/-103F, pressure at 7.18 hPa, daylight 05:27-17:21'
    """
    url = "https://twitter.com/marswxreport?lang=en"
    browser = fx_init_browser()
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    v_weather_list = [x.get_text().strip() for x in soup.find_all('div', {'class': 'js-tweet-text-container'})
                      if 'Sol' == x.get_text().strip().split(' ')[0]
                      ]
    v_weather_text = v_weather_list[0]
    global v_scrape_weather
    v_scrape_weather = v_weather_text
    return v_scrape_weather


def fx_scrape_fact():
    """
    output:
    [{'Equatorial Diameter:': '6,792 km'},
     {'Polar Diameter:': '6,752 km'},
     {'Mass:': '6.42 x 10^23 kg (10.7% Earth)'},
     {'Moons:': '2 (Phobos & Deimos)'},
     {'Orbit Distance:': '227,943,824 km (1.52 AU)'},
     {'Orbit Period:': '687 days (1.9 years)'},
     {'Surface Temperature:': '-153 to 20 °C'},
     {'First Record:': '2nd millennium BC'},
     {'Recorded By:': 'Egyptian astronomers'}]
    """
    url = "https://space-facts.com/mars/"
    v_table = pd.read_html(url)
    df_fact = v_table[0]
    v_list_of_dict = [{r[0]: r[1]} for i, r in df_fact.iterrows()]
    global v_scrape_fact
    v_scrape_fact = v_list_of_dict
    return v_scrape_fact


def fx_scrape_hemisphere():
    """
    output example: 
    [{'Equatorial Diameter:': '6,792 km'},
     {'Polar Diameter:': '6,752 km'},
     {'Mass:': '6.42 x 10^23 kg (10.7% Earth)'},
     {'Moons:': '2 (Phobos & Deimos)'},
     {'Orbit Distance:': '227,943,824 km (1.52 AU)'},
     {'Orbit Period:': '687 days (1.9 years)'},
     {'Surface Temperature:': '-153 to 20 °C'},
     {'First Record:': '2nd millennium BC'},
     {'Recorded By:': 'Egyptian astronomers'}]
    """
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser = fx_init_browser()
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    v_list_hemi = soup.find_all('div', {'class': 'item'})
    v_all_hemi_list_of_dict = []
    for list_hemi in v_list_hemi:
        v_data_dict = {}
        v_hemi_name = list_hemi.find_all('h3')[0].get_text()
        v_hemi_image_ref_suffix = list_hemi.find_all('a', {'class': 'itemLink product-item'})[0].get('href')
        v_hemi_image_ref = 'https://astrogeology.usgs.gov' + v_hemi_image_ref_suffix
        url = v_hemi_image_ref
        browser = fx_init_browser()
        browser.visit(url)
        time.sleep(1)
        html = browser.html
        soup = bs(html, "html.parser")
        v_download_hemi_container = soup.find_all('div', {'class': 'downloads'})[0]
        v_download_hemi_list = v_download_hemi_container.find_all('a', {'target': '_blank'})
        v_hemi_image_url_list = [x.get('href') for x in v_download_hemi_list if x.get_text() == 'Sample']
        v_hemi_image_url = v_hemi_image_url_list[0]
        v_data_dict = {'name': v_hemi_name, 'image_url': v_hemi_image_url}
        v_all_hemi_list_of_dict.append(v_data_dict)
    global v_scrape_hemisphere
    v_scrape_hemisphere = v_all_hemi_list_of_dict
    return v_scrape_hemisphere


def fx_scrape_image_url():
    """
    output example: 
    'https://photojournal.jpl.nasa.gov/jpeg/PIA17832.jpg'
    """
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser = fx_init_browser()
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")

    v_image_take1 = [x for x in soup.find_all('a', {'class': 'button fancybox'})][0]
    v_image_take1_url_suffix = v_image_take1['data-link']
    # sample https://www.jpl.nasa.gov/spaceimages/details.php?id=PIA17832

    url = 'https://www.jpl.nasa.gov' + v_image_take1_url_suffix
    browser = fx_init_browser()
    browser.visit(url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")
    v_image_take2 = soup.find_all('div', {'class': 'download_tiff'})
    v_image_take2_url_suffix = [x.find_all('a')[0].get('href') for x in v_image_take2 if
                                'JPG:' in x.get_text().split(' ')]
    v_image_high_res_url = 'https:' + v_image_take2_url_suffix[0]
    global v_scrape_image_url
    v_scrape_image_url = v_image_high_res_url
    return v_scrape_image_url


def fx_use_multithreading(*fx):
    """
    x = fx_use_multithreading(fx1,fx2)
    """
    max_thread = 5
    complete_thread_call_list = []
    Queue_thread_call_list = []
    cnt = 0
    for v_fx in fx:
        cnt += 1
        thread_name = 'master_thread_execution.' + str(cnt) + '.' + str(v_fx)
        thread_call = th(name=thread_name, target=v_fx)
        complete_thread_call_list.append(thread_call)
    cnt = 0

    if max_thread > len(complete_thread_call_list):
        max_thread = len(complete_thread_call_list)

    for x in complete_thread_call_list:
        next_run = True
        cnt += 1
        Queue_thread_call_list.append(x)
        if ((len(Queue_thread_call_list) < max_thread) and (cnt < len(complete_thread_call_list))):
            next_run = False

        if next_run == True:
            for t in Queue_thread_call_list:
                t.start()
            for t in Queue_thread_call_list:
                t.join()
            del Queue_thread_call_list[:]


def fx_scrape():
    """
    This will fetch and scrape info from external sites and insert into mongo db
    Example: fx_scrape()
    """
    fx_use_multithreading(fx_scrape_news, fx_scrape_weather, fx_scrape_fact, fx_scrape_hemisphere, fx_scrape_image_url)
    v_document_dict = {'list_time': dt.datetime.utcnow(),
                       'news': v_scrape_news,
                       'weather': v_scrape_weather,
                       'fact': v_scrape_fact,
                       'hemisphere': v_scrape_hemisphere,
                       'image_url': v_scrape_image_url}
    db.mars_log.insert_one(v_document_dict)
    return v_document_dict


def fx_fetch_latest_time_list(v_limit):
    """
    This will fetch last x documents from mongo
    Example: fx_fetch_latest_time_list(5)
    """
    cursor_t1 = db.mars_log.find({}, {'list_time': 1}).sort([("list_time", pymongo.DESCENDING)]).limit(v_limit)
    list_t1 = [{'_id': x['_id'], 'list_time': dt.datetime.strftime(x['list_time'], '%Y-%m-%d %H:%M:%S')} for x in
               list(cursor_t1)]
    v_latest_document_list_of_dict = list_t1
    return v_latest_document_list_of_dict


def fx_fetch_doc(v_id):
    """
    This will fetch document by its id from mongo
    Example: fx_fetch_doc(ObjectId('5ad67cb3e7191b637c3992c6'))
    """
    cursor_t1 = db.mars_log.find({'_id': v_id})
    dict_t1 = list(cursor_t1)
    v_document_dict = dict_t1[0]
    return v_document_dict
























































