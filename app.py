from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET'])
def query():
    url = request.args['url']
    
    newURL = getWikiImages(url)
    jsonURL = {
        'image-url' : newURL
        }
    return jsonURL
    

def getWikiImages(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("table", class_="infobox")
    for data in results:
        images = data.find('img')
    return str(images.get('src'))


if __name__ == '__main__':
    app.run() 

