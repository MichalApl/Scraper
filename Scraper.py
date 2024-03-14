import requests
from bs4 import BeautifulSoup
import time

def scraper():
    cookies = {
	## relevent cookies here if necessary
    }

    with open('<OUTPUT-FILE>', 'w') as file: 
            url = "<URL-HERE>"
                pageToScrape = requests.get(url, cookies=cookies)
                soup = BeautifulSoup(pageToScrape.text, "html.parser")
                objectToScrape = soup.findAll('<DESIRED HTML TAG>', attrs={'class': '<CLASS>'})

                for object in objectToScrape:
                    print(object.text)
                    file.write(object.text + '\n')
                    
                time.sleep(1) ## rate-limiting if necessary
                
            except Exception as e:
                print(f"Error scraping: {e}")

scraper()
