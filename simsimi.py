import cloudscraper
import json
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

scraper = cloudscraper.create_scraper()
load_dotenv('lang_code')
language = os.getenv("lang_code")

def simsimi(question):
  '''
  Function to make the HTTP request to the Simsimi API already with the message typed by the user
  '''

  url = f'https://api.simsimi.net/v1/?text={question}={language}' #Language code (vi, en, ph, zh, ch, ru, id, ko, ar, fr, ja, es, de, pt, ...)

  #bypass cloudflare antibot fetch
  response = scraper.get(url).text
  soup = BeautifulSoup(response, 'html.parser')

  #debug stuff
  #print("Code: " + str(soup))

  text = json.loads(soup.text)
  return text["success"] # Return the reply message