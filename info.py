import whois
import moment
import time
from datetime import datetime

def getAge(url):
	w = whois.whois(url)
	creation_date = None
	if isinstance(w.creation_date, list):
		creation_date = w.creation_date[0]
	else:
		creation_date = w.creation_date
	date = moment.date(creation_date, '%Y-%m-%d %H:%M:%S')

	current_timestamp = time.time()
	creation_timestamp = date.epoch()

	final_timestamp = current_timestamp - creation_timestamp

	return datetime.fromtimestamp(final_timestamp).month