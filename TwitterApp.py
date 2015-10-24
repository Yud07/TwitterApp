#!/usr/bin/python -u

import twitter

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

api = twitter.Api(consumer_key, consumer_secret, access_key, access_secret)

def post():
	"""Post a message to twitter"""
	message = raw_input("What would you like to say: ")
	if len(message) > 140:
		overrun = len(message) - 140
		print "That was", overrun, "characters too long. Try again.\n"
		post()
	else:
		if ascii(message):
			status = api.PostUpdate(message)
			print "%s just posted: %s" % (status.user.name, status.text)
		else:
			print "All characters must be ASCII. Try again.\n"
			post()
			

def search():
	"""Search twitter posts and DMs."""
	print "What would you like to search?\n1. Tweets\n2. Tweets from Person\n3. Tweets to Person"
	searchType = raw_input("Enter search type 1-3: ")
	if searchType.isdigit() == False and searchType < 4 and searchType < 0:
		print "Please enter an integer 1-3\n"
		search()
	else:
		searchType = int(searchType)	
	phrase = raw_input("Enter the phrase you would like to search: ")
	if len(phrase) > 140:
		overrun = len(phrase) - 140
		print "That was", overrun, "characters too long. Try again.\n"
		search()
	else:
		if ascii(phrase):
			if searchType == 1:
				results = api.GetSearch(term=phrase, lang='en')
				for s in results:
					print "%s posted: %s" % (s.user.name, s.text)
			elif searchType == 2:
				print "Would you like to search by:\n1. User ID\n2. Screen Name"
				nameType = raw_input("Enter name type 1-2: ")
				if nameType.isdigit() == False and nameType < 3 and nameType < 0:
					print "Please enter an integer 1-2\n"
					search()
				else:
					nameType = int(nameType)
				if nameType == 1:
					uid = raw_input("Enter the User ID you would like to search for: ")
					if len(uid) > 15:
						overrun = len(uid) - 15
						print "That was", overrun, "characters too long. Try again.\n"
						search()
					else:
						results = api.GetUserTimeline(user_id = uid)
						for s in [s for s in results if s.text.find(phrase) != -1]:
							print "%s posted: %s" % (s.user.name, s.text)
				elif nameType == 2:
					sn = raw_input("Enter the Screen Name you would like to search for: ")
					if len(sn) > 15:
						overrun = len(sn) - 15
						print "That was", overrun, "characters too long. Try again.\n"
						search()
					else:
						if ascii(sn):
							results = api.GetUserTimeline(screen_name = sn)
							for s in [s for s in results if s.text.find(phrase) != -1]:
								print "%s posted: %s" % (s.user.name, s.text)
						else:
							print "All characters must be ASCII. Try again.\n"
							search()
			elif searchType == 3:
				uid = raw_input("Enter the User ID you would like to search for: ")
				if len(uid) > 15:
					overrun = len(uid) - 15
					print "That was", overrun, "characters too long. Try again.\n"
					search()
				else:
					results = api.GetSearch(term=uid, lang='en')
					for s in [s for s in results if s.text.find(phrase) != -1 and s.text.find("RT") == -1]:
						print "%s posted: %s" % (s.user.name, s.text)
		else:
			print "All characters must be ASCII. Try again.\n"
			search()

def ascii(s):
	"""Does this string contain only ascii characters?"""
	return all(ord(c) < 128 for c in s)

def main():
	while True:
		print "Would you like to:\n1. Post\n2. Search\n3. Exit"
		actionType = raw_input("Enter action type 1-3: ")
		if actionType.isdigit() == False and actionType < 4 and actionType < 0:
			print "Please enter an integer 1-3\n"
		else:
			actionType = int(actionType)
		if actionType == 1:
			post()
		elif actionType == 2:
			search()
		elif actionType == 3:
			break
main()
