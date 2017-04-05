import json
import urllib2
import sys

city = raw_input("Please select a city to view some weather details: ")


# open the url and the screen name 
# (The screen name is the screen name of the user for whom to return results for)
try:
	url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&APPID=d16c3568597c640bba3c07d5b1893707"
	# this takes a python object and dumps it to a string which is a JSON
	# representation of that object
	data = json.load(urllib2.urlopen(url))
	
	# print the result
	# print data
	# print json.dumps(data, indent=4, sort_keys=True)

	print "Name of City:", data['name'],"\n"
	print "Weather:\n"
	print "Humidity: ", data['main']['humidity'],"\n"

except:
	print "Wrong city entered"