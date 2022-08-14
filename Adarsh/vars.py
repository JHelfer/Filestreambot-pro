# (c) jhelfer
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
	MULTI_CLIENT = False
	API_ID = str(getenv('18732376'))
	API_HASH = str(getenv('738479feb6d6215c1d3a64222daa7ba8'))
	BOT_TOKEN = str(getenv('5397911007:AAGRNMnMh-Aa3DCcrm8D0UaZHxL-YSJNEH4'))
	name = str(getenv('name', 'filetolinkbot'))
	SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
	WORKERS = int(getenv('WORKERS', '4'))
	BIN_CHANNEL = int(getenv('1001660090671'))
	PORT = int(getenv('PORT', 8080))
	BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
	PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200")) # 20 minutes
	OWNER_ID = set(int(x) for x in os.environ.get("20838550747", "").split())
	NO_PORT = bool(getenv('NO_PORT', False))
	APP_NAME = None
	OWNER_USERNAME = str(getenv('enjoy_jer'))
	if 'DYNO' in environ:
		ON_HEROKU = True
		APP_NAME = str(getenv('enjoyjer-telebot'))
	else:
		ON_HEROKU = False
	fQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
	HAS_SSL=bool(getenv('HAS_SSL',False))
	if HAS_SSL:
		URL = "https://{}/".format(fQDN)
	else:
		URL = "http://{}/".format(fQDN)
	DATABASE_URL - str(getenv('mongodb+srv://use:lok@cluster0.mc9jg5k.mongodb.net/?retryWrites=true&w=majority'))
	UPDATES_CHANNEL = str(getenv('FStreamJoin', None))
	BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
