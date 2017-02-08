from bs4 import BeautifulSoup
from collections import namedtuple
import json
import urllib.request

url = 'http://gd2.mlb.com/components/game/mlb'
gameList = []
#Format (MM/DD/YYYY)
class MLBData():
	global gameList 
	def __init__(self, date):
		self.url = url + '/year_' + date.split('/')[2] + '/month_' + date.split('/')[0] + '/day_' + date.split('/')[1] + '/master_scoreboard.json'
		page = urllib.request.urlopen(self.url)
		soup = BeautifulSoup(page,'html.parser')
		self.json = soup.get_text()
		self.parseJson(self.json)

	def parseJson(self,jsonData):
		jsonData = json.loads(jsonData)
		games = jsonData['data']['games']['game']
		for game in games:
			game = json.dumps(game)
			gameList.append(json.loads(game, object_hook=lambda d: namedtuple('X', d.keys())(*d.values())))
	def getTeamData(self, teamName):
		for game in gameList:
			if teamName.lower() == game.home_name_abbrev.lower() or teamName.lower() == game.away_name_abbrev.lower():
				return game
		return 'No Game Found'

