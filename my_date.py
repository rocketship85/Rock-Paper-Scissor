from urllib2 import Request, urlopen, URLError
import json
import time

print (time.strftime("%Y-%m-%d"))
current_date = time.strftime("%Y-%m-%d")
zip_code = "94568"



request = Request("http://data.tmsapi.com/v1.1/movies/showings?startDate=" + current_date + "&zip=" + zip_code + "&api_key=ux6gr9kf8meph2nwxvpzq3pa")

response = urlopen(request)
results = response.read()
shows = json.loads(results)


for item in shows:
	print item["title"]
	for item2 in item["showtimes"]:
		print item2["theatre"]["name"] + " " + item2["dateTime"]



request = Request("https://api.yelp.com/v2/search/?term=restaurant&location=94568")

response = urlopen(request)
results = response.read()
restaurants = json.loads(results)

for restaurant in restaurants["businesses"]:
	print restaurant["name"]

 