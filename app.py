from flask import *
from flask import jsonify
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
		#print request.form.get("query", "")
		if app.config['NYTIMES_API_KEY']:
			# iterate through pages
			title_list = []
			for i in range(0, 10):
				#app.config['API_PAGE'] = str(i)
				api_request = requests.get(app.config['API_PATH'] + request.form.get("query", "") + app.config['API_PAGEDEF'] + str(i) + app.config['API_PATH2'] + app.config['NYTIMES_API_KEY'])
	#			print api_request
				if api_request.status_code == 200:
					json_response = api_request.json()
					if json_response:
						# 10 articles per page
						for x in range (0,10):
							article_title = json_response['response']['docs'][x]['headline']['main']
							title_list.append(article_title)
							print "TITLE#"+str(i)+", "+str(x)+": "+article_title
	#				       		return jsonify(json_response)
					else:
						print "json_response no"
	#				return jsonify(json_response)
				else:
					print "api_request no"
			### Call Justin's Poem Stuff                                      
			print "Poem!"
			print PG.getPoem(title_list)
			return "<br> ".join(PG.getPoem(title_list))
		else:
			print "config error"
	#	return "we good"
	else:
		return redirect('/')

@app.route('/about', methods=['GET'])
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)
