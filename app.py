from flask import Flask, render_template
import requests
from newsapi import NewsApiClient

app = Flask(__name__)

# Init
newsapi = NewsApiClient(api_key='70fdb9ba81ba40b6bda148e672898bd9')

@app.route("/")
def home():
	return render_template("home.html")

@app.route("/top-headlines")
def headlines():
	top_headlines = newsapi.get_top_headlines(country="in")['articles']
	return render_template("top_headlines.html", all_headlines = top_headlines)


if __name__ == "__main__":
	app.run(debug = True)