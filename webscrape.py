from bs4 import BeautifulSoup
import requests

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=36.46458&lon=-79.762539")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp temp-low").get_text()
print temp
              
