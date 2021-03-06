
import botkit
import requests
import redis
import re

REDIS_KEY = 'ingress-googleplay-lastupdate'
URL = 'https://play.google.com/store/apps/details?id=com.nianticproject.ingress'

resp = requests.get(URL)
m = re.search('<div class="document-subtitle">(.*?)<', resp.text)
date = m.group(1)

rc = redis.StrictRedis()
last = rc.get(REDIS_KEY)
rc.set(REDIS_KEY, date)

if date != last:
    bot = botkit.Bot(username='GooglePlay')
    bot.send('Update: last update', date)
