from flask import Flask, render_template, request
from newsapi import NewsApiClient

app = Flask(__name__)

# Init
newsapi = NewsApiClient(api_key='70fdb9ba81ba40b6bda148e672898bd9')

@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == "POST":
		all_sources = newsapi.get_sources()['sources']
		sources = []
		domains = []
		for e in all_sources:
			id = e['id']
			domain = e['url'].replace("http://", "")
			domain = domain.replace("https://", "")
			domain = domain.replace("www.", "")
			slash = domain.find('/')
			if slash != -1:
				domain = domain[:slash]
			sources.append(id)
			domains.append(domain)
		sources = ", ".join(sources)
		domains = ", ".join(domains)
		# print(sources)
		# print(domains)
		keyword = request.form["keyword"]
		all_articles = newsapi.get_everything(q=keyword,
                                      sources=sources,
                                      domains=domains,
                                      language='en',
                                      sort_by='relevancy')['articles']
		# all_headlines = newsapi.get_top_headlines(country="in", language="en")['articles']
		return render_template("home.html", all_headlines = all_articles)
	else:
		all_headlines = newsapi.get_top_headlines(country="in", language="en")['articles']
		return render_template("home.html", all_headlines = all_headlines)
	return render_template("home.html")

@app.route("/query/<string:keyword>/")
def query(keyword):
	pass

@app.route("/page/<int:page_no>/")
def page(page_no):
	pass

if __name__ == "__main__":
	app.run(debug = True)