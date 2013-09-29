from flask import Flask
from flask import jsonify
import requests
import helper.poemGenerator as PG

app = Flask(__name__)

app.config['NYTIMES_API_KEY'] = "4b7f1044c821ae86af829a6a53f4e1c8:11:68190060"
app.config['API_PATH'] = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=economy&api-key="

@app.route('/', methods=['GET'])
def hello_world():
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

				### Call Justin's Poem Stuff
				print "Poem!"
				print PG.getPoem(title_list)
				return "<br> ".join(PG.getPoem(title_list))

#				return jsonify(json_response)
			else:
				print "json_response no"
		else:
			print "api_request no"
	else:
		print "config error"

if __name__ == '__main__':
	app.run(debug=True)
