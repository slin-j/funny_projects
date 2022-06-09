import time
import os

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
from bs4.element import Comment

FIREFOX_DRIVER = os.path.join(os.path.dirname(__file__), 'firefox', 'geckodriver.exe')
FIREFOX_LOG = os.path.join(os.path.dirname(__file__), 'firefox', 'geckodriver.log')

def get_all_addresses(comparis_url:str) -> list:
    advert_counter = 1e9
    result_addresses = []
    result_links = []
    pageProgess = 0
    
    # create browser instance
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(
        executable_path=FIREFOX_DRIVER,
        service_log_path=FIREFOX_LOG,
        options=options
    )

    while advert_counter > 0:
        # read site 
        browser.get(f'{comparis_url}&page={pageProgess}')
        time.sleep(1)

        # scroll to bottom
        body = browser.find_element(by=By.CSS_SELECTOR, value='body')
        for i in range(4):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.5)
        
        # parse to html
        sitecontent = BeautifulSoup(browser.page_source, 'html.parser')

        if pageProgess == 0:
            # find out how many adverts there are -> only 10 per chapter
            texts = sitecontent.findAll(text=True)

            def tag_visible(element):
                if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
                    return False
                if isinstance(element, Comment):
                    return False
                return True

            visible_text = filter(tag_visible, texts)
            site_text = " ".join(t.strip() for t in visible_text)

            stop = site_text.find("Treffer")-1
            start = stop - 1
            while site_text[start] != ' ': start -= 1
            
            advert_counter = int(site_text[start:stop:])

        # for every advert on the page
        for ae in sitecontent.find_all('a', {'class' : 'css-a0dqn4 ehesakb1'}):
            # find address and append to return list
            result_addresses.append(ae.find_all('p', {'class' : 'css-a7uk28 ehesakb2'})[0].find(text=True))
            
            # find advert-id, generate link to advert and append to list
            result_links.append('https://www.comparis.ch' + ae.get('href'))
        
            advert_counter -= 1
        
        pageProgess += 1
        
    browser.quit()
    print('len result_addersses: ', len(result_addresses))
    return result_addresses, result_links