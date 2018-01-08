import requests
import json
import csv
import time
import schedule
#import pynotify

import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

#Adding all new Streams to CSV file, To check for any duplicates
def add_live(liveId, name, url, imageUrl, genre):
	data = [liveId, name, url, imageUrl, genre]
	with open("sonylivData.csv", "a") as fp:
	    wr = csv.writer(fp, dialect='excel')
	    wr.writerow(data)

#Function To get all saved Streams Details
def getLiveDatas():
	liveDatas = []
	try:
		r = csv.reader(open('sonylivData.csv'))
		liveDatas = [l for l in r]
	except:
		print 'No CSV Found'
	return liveDatas

#Notify Ubuntu Users with Pynotify
def popup(title, message):
    pynotify.init("Test")
    pop = pynotify.Notification(title, message)
    pop.show()
    return

sonyLivUrl = 'http://www.sonyliv.com/api/v2/vod/search'

def extractSonyLivDataLive():
	try:
		payload = '{"searchSet":[{"data":"all=classification:sport&all=type:live","type":"search","action":"sony://player","pageSize":10,"pageNumber":0,"id":"live_matches_band","sortOrder":"START_DATE:DESC"},{"data":"all=classification:sport&all=tag:indsa2018liv","type":"search","action":"","pageSize":10,"pageNumber":0,"id":"ind_sa2018","sortOrder":"START_DATE:DESC"},{"data":"4686191111001","type":"playlist","action":"","pageSize":10,"pageNumber":0,"id":"latest_episodes","sortOrder":"START_DATE:DESC"},{"data":"all=type:show&none=classification:sport","type":"search","action":"","pageSize":10,"pageNumber":0,"id":"show_allshows_band","sortOrder":"START_DATE:DESC"},{"data":"5282651858001","type":"playlist","action":"","pageSize":1,"pageNumber":0,"id":"banner_playlist_16","sortOrder":"DISPLAY_NAME:ASC"},{"data":"5283543277001","type":"playlist","action":"sony://internal/selectPack","pageSize":1,"pageNumber":0,"id":"banner_playlist_15","sortOrder":"DISPLAY_NAME:ASC"},{"data":"4923607986001","type":"playlist","action":"","pageSize":1,"pageNumber":0,"id":"banner_playlist_1","sortOrder":"DISPLAY_NAME:ASC"},{"data":"4923889158001","type":"playlist","action":"","pageSize":1,"pageNumber":0,"id":"banner_playlist_2","sortOrder":"DISPLAY_NAME:ASC"},{"data":"4923607987001","type":"playlist","action":"","pageSize":1,"pageNumber":0,"id":"banner_playlist_3","sortOrder":"DISPLAY_NAME:ASC"},{"data":"4923607988001","type":"playlist","action":"","pageSize":1,"pageNumber":0,"id":"banner_playlist_4","sortOrder":"DISPLAY_NAME:ASC"},{"data":"4923889159001","type":"playlist","action":"","pageSize":1,"pageNumber":0,"id":"banner_playlist_5","sortOrder":"DISPLAY_NAME:ASC"},{"data":"4923889160001","type":"playlist","action":"","pageSize":1,"pageNumber":0,"id":"banner_playlist_6","sortOrder":"DISPLAY_NAME:ASC"}],"detailsType":"basic","deviceDetails":{"mfg":"Google Chrome","os":"others","osVer":"XXX","model":"Google Chrome","deviceId":84482736481}}'
		headers = {'Content-Type':'application/json;charset=UTF-8','Cookie':'ajs_anonymous_id=%221880759e-5b46-487b-865c-9400ea41d6ee%22; _cbsk=e4754e30-afd4-11e7-a65c-4feed5d32845; _rsid=84482736481; userLoc=%22%22; G_ENABLED_IDPS=google; wurfljs_ch_65e232ed43477b2f5cb4413023548fce=1508265804081; WZRK_G=37bb236fb72a4d369fb4e2604b1711f4; _ga=GA1.2.7775858.1508489367; __gads=ID=f69efbe789dd7cfe:T=1508489362:S=ALNI_MZmsKGokc1pWbt3qQn4ALAISAG-9A; wurfljs_ch_e6b04c8770df66c68b46b9485d45dc74=1508553408976; ajs_user_id=null; ajs_group_id=null; xdrItems=[]; currentXdrItem=null; profLookup=[%22ek%20tha%20tiger%22]; WZRK_L=http%3A%2F%2Fwzrkt.com%2Fa%3Ft%3D78%26type%3Dpush%26d%3DN4IgLgngDgpiBcIYDcYDswgDROWAcgIYC2cihUUA%252BjAB4CWmOKYAIoWIQqHY1WPVIIAjAFZhAFgCcUgEwB2UQDZhMnAFcAzjABOVegBMEIABwSJJhQGYlF4dhCEDqHQM300AcwCSRxAHEAQWEAOlkQ%252BUjRE2iQsQAGMxMpG3kHF3cAezRjUNEQqwcAYwALQjQ0GAAbYwB3GAAjEABfHENjCwBpAFoTAHU%252B7sUJAC0HT2MreQaG2RsAMwb5WUIJAxspRYkYWSV4iQbheWFheYkHKAn4WRwDTQg0IoQwHXUYHD6RgCVOqgBhQIAWQACtwQLViFAEPEcGAqk94ABtAC6zWaQAA%253D%7C%24%7C1514992756; _cks=s%3AMUDySzvXOEEyrfk7VscQL9iD.BcY1n9RSLbrwiFHzWWCurDsudB0CFhr0Fus5f%2BWBMGU; LastUpdatedTime=2018-01-08%2019:39:49; XSRF-TOKEN=7dZttEdc-UCQhbQqny3Jl0tKHAaINLtdyL4Q; AppStartTime=2018-01-08%2019:39:53; WZRK_S_48K-8WW-754Z=%7B%22p%22%3A4%7D"}','X-XSRF-TOKEN':'7dZttEdc-UCQhbQqny3Jl0tKHAaINLtdyL4Q'}
		response = requests.request("POST", sonyLivUrl, data=payload, headers=headers)
		if response.status_code == 200:
			joke_text = json.loads(response.content.decode())
			for jsont in joke_text:
				if jsont['id'] == "live_matches_band":
					count = 0
					for singleLiv in jsont['assets']:
						contentId = singleLiv['id']
						contentName = singleLiv['title']
						contentImage = singleLiv['thumbnailUrl']
						contentGenre = singleLiv['genre']
						if contentImage == 'None' or contentImage == None:
							continue
						alreadyAdded = False
						liveDatas = getLiveDatas()
						for liveData in liveDatas:
							if str(contentId) == liveData[0] and str(contentName) == liveData[1]:
								alreadyAdded = True
								kattappaLiveId = liveData[3]
								break
							else:
								alreadyAdded = False
						if alreadyAdded != True:
							add_live(contentId, contentName, contentId, contentImage, contentGenre)
							#Uncomment Below line to Get Notification in Ubuntu
							#popup("New SonyLiv Stream Started", str(contentName) + ' - ' + str(contentGenre))
							print "New Live Started in SonyLiv : " + str(contentName) + " (" + str(contentGenre) + ")"
					print "Done Extracting Live URLs from SonyLiv"
		else:
			print "No Live Streams Found in SonyLIV"
	except:
		print "Some Error in Parsing the Response"

#Schedule the function to run it every 5 mins
schedule.every(5).minutes.do(extractSonyLivDataLive)
while 1:
	schedule.run_pending()
	time.sleep(1)