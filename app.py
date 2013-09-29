from flask import *
import requests
import helper.poemGenerator as PG
from generateaudio import generateAudio
import os

app = Flask(__name__)

app.config['NYTIMES_API_KEY'] = "4b7f1044c821ae86af829a6a53f4e1c8:11:68190060"
app.config['API_PATH'] = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q="
app.config['API_PAGEDEF'] = "&page="
app.config['API_PATH2']="&api-key="

@app.route('/', methods=['GET'] )
def welcome():
	return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def hello_world():
	if request.method == 'POST':
		if app.config['NYTIMES_API_KEY']:
			# iterate through pages
			title_list = []
			for i in range(0, 10):
				api_request = requests.get(app.config['API_PATH'] + request.form.get("query", "") + app.config['API_PAGEDEF'] + str(i) + app.config['API_PATH2'] + app.config['NYTIMES_API_KEY'])
				if api_request.status_code == 200:
					json_response = api_request.json()
					if json_response:
						# 10 articles per page
						for x in range (0,10):
							article_title = json_response['response']['docs'][x]['headline']['main']
							article_title = article_title.encode('ascii','ignore')
							title_list.append(article_title)
					else:
						print "Not getting the right JSON!"
				else:
					print "Status Code is not 200."
			### Call Justin's Poem Stuff                                      
			lyrics = Markup(".<br>".join(PG.getPoem(title_list))+"." )
			web_url = generateAudio(" ".join(PG.getPoem(title_list)), int(request.form.songSelect()))
			return render_template('results.html', lyrics=lyrics, web_url=web_url)
		else:
			print "Error with API Key config."
	else:
		return redirect('/')

@app.route('/about', methods=['GET'])
def about():
	return render_template('about.html')

if __name__ == '__main__':
	port = int(os.environ.get("PORT", 5000))
	if port == 5000:
		app.debug = True
	app.run(host='0.0.0.0', port=port)
