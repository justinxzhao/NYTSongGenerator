from flask import *
import requests
import helper.poemGenerator as PG

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
							title_list.append(article_title)
					else:
						print "Not getting the right JSON!"
				else:
					print "Status Code is not 200."
			### Call Justin's Poem Stuff                                      
			lyrics = Markup("<br>".join(PG.getPoem(title_list)))
			web_url = "https://api.sonicapi.com/process/elastiqueTune?access_id=78908f19-88ab-4e11-ab95-ac47aecd8458&input_file=http://media.tts-api.com/faa17ba12cd76886d3ebba1f92392994a6387b18.mp3&tempo_factor=0.75&pitchcorrection_percent=80&pitchdrift_percent=100&midi_pitches=58-58-58-58-58-58-57-57-53-57-55-53-58-57-57-53-57-55-53-58-57-57-53-53-57-55-55-53-57-55-53-58-53-53-53-57-55-55-53-58-..."
			return render_template('results.html', lyrics=lyrics, web_url=web_url)
		else:
			print "Error with API Key config."
	else:
		return redirect('/')

@app.route('/about', methods=['GET'])
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)
