import urllib, json, time, csv
searchUrl = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
api_key = 'AIzaSyCaKmIf4fLDedCeidrzdes-n18MzcGje9M'

curState = None
curStateCount = 1
curLat = 0.0
curLng = 0.0

#opening various files
zipstates = open('zipStates.csv', 'rb')
jewCOM = open('jewCOM.csv', 'w')
writer = csv.writer(jewCOM, delimiter=',')


reqMade=0
first=1

for row in zipstates:
	print(reqMade)#just displays the number of request made
	zip,state = row.split(',')

	#keeps taking items from the list till it finds another state
	if (state == '"Hawaii"' or state == '"Alaska"'):
		continue
	#initial request	
	MyUrl = ('%squery=jewlery+stores+in+%s&key=%s' % (searchUrl, zip, api_key))
	reqMade+=1
	response = urllib.urlopen(MyUrl)
	jsonRaw = response.read()
	jsonData = json.loads(jsonRaw)

	#adds lat and lng of all stores in the json
	for store in range(1, len(jsonData['results'])):
		curLat = jsonData['results'][store]['geometry']['location']['lat']
		curLng = jsonData['results'][store]['geometry']['location']['lng']
		writer.writerow([state, str(curLat), str(curLng)])

	#if there are more then one page on last query then get next page until no more pages
	while ('next_page_token' in jsonData and jsonData['next_page_token']!=None):
		time.sleep(2)#have to wait a couple seconds before asking for page
		MyUrl=('%spagetoken=%s&key=%s' % (searchUrl, jsonData['next_page_token'], api_key))
		reqMade+=1
		print('next page')
		response = urllib.urlopen(MyUrl)
		jsonRaw = response.read()
		jsonData = json.loads(jsonRaw)
		
		#adds lat and lng of all stores in the json
		for store in range(1, len(jsonData['results'])):
			curLat = jsonData['results'][store]['geometry']['location']['lat']
			curLng = jsonData['results'][store]['geometry']['location']['lng']
			writer.writerow([state, str(curLat), str(curLng)])


print('YOU HAVE FINISHED!!!! HURRAY!!!')