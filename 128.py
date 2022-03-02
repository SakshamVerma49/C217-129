import csv
from attr import attrs
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

start_url = "https://exoplanets.nasa.gov/exoplanet-catalog/"

browser = webdriver.Chrome("D:/Users/Saksham.Admin-PC/WhiteHatjr/C127/chromedriver.exe")

browser.get(start_url)

time.sleep(10)

headers = ["name", "light_years_from_earth", "planet_mars", "stellar_magnitude", "discovery_date", "hyperlink", "planet_type", "planet_radius", "orbital_radius", "orbital_period"]
planet_data = []

new_planet_data = []

def scrape():
    for i in range(0, 5):

        time.sleep(2)

        soup = BeautifulSoup(browser.page_source, "html.parser")

        for ul_tag in soup.find_all("ul", attrs = {"class", "exoplanet"}):

            li_tags = ul_tag.find_all("li")
            temp_list = []
            
            for index, li_tag in enumerate(li_tags):

                if(index == 0):
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:

                    try:
                        temp_list.append(li_tag.contents[0])
                    
                    except:

                        temp_list.append("")
            hyperlink_li_tag = li_tags[0]
            temp_list.append("https://exoplanets.nasa.gov" + hyperlink_li_tag.find_all("a", href = True)[0]["href"])
            planet_data.append(temp_list)

        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("Scraper.csv", "w") as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(planet_data)

def scrapeMoreData(hyperlink):
    try:

        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content, "html.parser")
        temp_list = []

        for tr_tag in soup.find_all("tr", attrs = {"class": "fact_row"}):

            td_tags = tr_tag.find_all("td")

            for td_tag in td_tags:

                try:
                    
                    temp_list.append(td_tag.find_all("div", attrs = {"class": "value"})[0].contents[0])
                
                except:
                    
                    temp_list.append('')
        
        new_planet_data.append(temp_list)

    except:

        time.sleep(1)
        scrapeMoreData(hyperlink)

scrape()

for index, data in enumerate(planet_data):
    scrapeMoreData(data[5])

final_planet_data = []

for index, data in enumerate(planet_data):

    new_planet_data_element = new_planet_data[index]
    new_planet_data_element = [data_element.replace("\n", '') for data_element in new_planet_data_element]
    new_planet_data_element = new_planet_data_element[:7]

    final_planet_data.append(data + new_planet_data_element)

with open("Final Scraper.csv", "w") as f:
    
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(final_planet_data)