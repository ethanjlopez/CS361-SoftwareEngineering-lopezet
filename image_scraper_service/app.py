from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/', methods=['GET'])
@cross_origin()
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
    results = soup.select('table[class*="infobox"] img')
    if results == []:
        results = soup.find_all("div", "thumbinner", limit=1)
        if results != []:
            for data in results:
                images = data.find('img')
            return str(images.get('src'))
        else:
            return "No Picture Available"
    return(results[0]['src'])


if __name__ == '__main__':
    app.run() 

