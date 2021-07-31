A Flask Web API that image scrapes the first image from Wikipedia when given the url as a query string  and returns it in JSON format. 

Sample Request:

(GET):

/?url=https://en.wikipedia.org/wiki/Bluebird

Sample Response:

{
"image-url": "//upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Eastern_Bluebird.jpg/220px-Eastern_Bluebird.jpg"
}