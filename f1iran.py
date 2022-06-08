from cgitb import text
from http.client import FORBIDDEN
import requests
from bs4 import BeautifulSoup
from newspaper import Article
from tqdm import tqdm
import pandas as pd

def repeatitive(links, urls):
    for link in links:
        if link.a['href'] in urls:
            return True 
    return False

def scraping():

    page = 540
    scrapted_data = []
    url_list = []

    while True:
        page += 1
        main_page_URL = f"https://f1iran.com/category/formula1/last_f1_news/page/{page}/"
        page_HTML = requests.get(main_page_URL).text

        soup = BeautifulSoup(page_HTML, features='lxml')

        links = soup.find_all('h2')

        if repeatitive(links, url_list):
            break

        for link in tqdm(links):
            page_url = link.a['href']
            url_list.append(page_url)
            try:
                article = Article(page_url)
                article.download()
                article.parse()
                newsarticle = {
                    'title' : article.title,
                    'usrlss' : page_url,
                    'text' :article.text
                    }
                scrapted_data.append(newsarticle)
            except:
                print(f"Failed to process page {page_url}")
        
    df = pd.DataFrame(scrapted_data)
    df.to_csv('F1Iran.csv')
 

