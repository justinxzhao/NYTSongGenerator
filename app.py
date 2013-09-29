from flask import Flask
from flask import jsonify
import requests
import urllib2
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

app.config['NYTIMES_API_KEY'] = "4b7f1044c821ae86af829a6a53f4e1c8:11:68190060"
app.config['API_PATH'] = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=economy&api-key="

def visible(element):
	if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:
		return False
	elif re.match('<!--.*-->', str(element)):
		return False
	return True

@app.route('/', methods=['GET'])
def hello_world():
#        return 'Hello World!'
#	url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?fq=romney&facet_field=day_of_week&begin_date=20120101&end_date=20120101&api-key=4b7f1044c821ae86af829a6a53f4e1c8:11:68190060"
	loc = 0;
	if app.config['NYTIMES_API_KEY']:
		api_request = requests.get(app.config['API_PATH'] + app.config['NYTIMES_API_KEY'])
		if api_request.status_code == 200:
			json_response = api_request.json()
			if json_response:
				title_list = []
				for x in range (0,9):
					article_title = json_response['response']['docs'][x]['headline']['main']
					title_list.append(article_title)
					print article_title
#				return jsonify(json_response)
			else:
				print "json_response no"
		else:
			print "api_request no"
	else:
		print "config error"

if __name__ == '__main__':
	app.run(debug=True)
