import requests
import datetime
#from bs4 import BeautifulSoup

now = datetime.datetime.now()
hour = now.hour

while True:
    now = datetime.datetime.now()
    current_hour = now.hour
    if 6 < current_hour < 22 and hour < current_hour:
        #page = requests.get('https://sinoptik.ua/')
        #soup = BeautifulSoup(page.text, 'lxml')
        #temperature_tag = soup.find('p', {'class':'today-temp'})
        #temperature = temperature_tag.get_text()
        #requests.get('https://api.telegram.org/bot383163486:AAF5llYAvHZqCkdF4H6FQegwhJQCbUFfjic/sendMessage?chat_id=385220023&text={}'.format(temperature))
        requests.get('https://api.telegram.org/bot383163486:AAF5llYAvHZqCkdF4H6FQegwhJQCbUFfjic/sendMessage?chat_id=385220023&text={}'.format(current_hour))
        hour = current_hour
    
    

