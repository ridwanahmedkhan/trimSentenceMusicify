from twython import Twython
import json
from MyCredentials import MyCredentials
from MidiConverter import MidiConverter

class TweetMusicify:
	
	TWITTER_APP_KEY = '';
	TWITTER_APP_KEY_SECRET = ''
	TWITTER_ACCESS_TOKEN = ''
	TWITTER_ACCESS_TOKEN_SECRET = ''
	
	def __init__(self):
		mycred = MyCredentials()
		self.TWITTER_APP_KEY = mycred.TWITTER_APP_KEY
		self.TWITTER_APP_KEY_SECRET = mycred.TWITTER_APP_KEY_SECRET 
		self.TWITTER_ACCESS_TOKEN = mycred.TWITTER_ACCESS_TOKEN
		self.TWITTER_ACCESS_TOKEN_SECRET = mycred.TWITTER_ACCESS_TOKEN_SECRET
		
	def tweet_to_music(self):
		t = Twython(app_key=self.TWITTER_APP_KEY, 
				app_secret=self.TWITTER_APP_KEY_SECRET, 
				oauth_token=self.TWITTER_ACCESS_TOKEN, 
				oauth_token_secret=self.TWITTER_ACCESS_TOKEN_SECRET)

		search = t.search(q='#DonaldTrump',count=5)
		tweets = search['statuses']

		midiConverter = MidiConverter()
		for tweet in tweets:
			print tweet['id_str'], '\n', tweet['text'], '\n\n\n'
			tweetString = tweet['text'].encode("utf8")
			midiConverter.stringToMidiConverter(tweetString)
