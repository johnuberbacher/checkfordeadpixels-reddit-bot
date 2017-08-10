import praw
import config
import time
import os

print ("Importing dependencies...")
def bot_login():
	print ("Logging in...")
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = config.user_agent)
	print("Logged in...")
	return r
	
def run_bot(r, cached_comments):
	print ("Scanning comments...")
	
	for comment in r.subreddit('all').comments(limit=50):
		if "dead pixel" in comment.body and comment.id not in cached_comments and  comment.author != r.user.me():
			print("Instance of \"dead pixel(s)\" found in comment {}.".format(comment.id))
			comment.reply("I am a bot, *bleep, bloop.* Somebody mention dead pixels? \n\n [checkfordeadpixels.com](http://checkfordeadpixels.com) is the easiest and least automated way to check for dead pixels.\n***\n^^checkfordeadpixels ^^is ^^non ^^monitzed ^^and ^^has ^^no ^^ads, ^^it's ^^totally ^^free ^^and ^^open ^^source!")
			print("Replied to comment ID: {}.".format(comment.id))
			cached_comments.append(comment.id)
			
			with open ("cached_comments.txt", "a") as f:
				f.write(comment.id + "\n")
	
	print ("Sleeping for 12 hours...")
	time.sleep(43200)
	
def get_cached_comments():
	if not os.path.isfile("cached_comments.txt"):
		cached_comments = []
	else:
		with open("cached_comments.txt", "r") as f:
			cached_comments = f.read()
			cached_comments = cached_comments.split("\n")
		
	return cached_comments

r = bot_login()
cached_comments = get_cached_comments()

while True:
	run_bot(r, cached_comments)