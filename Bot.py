import praw
import random

REPLY_STRING = "Now that's 'a spiccy meat 'ta ball! I give it a {} out of 10!"

reddit = praw.Reddit(user_agent='Spiccymeat',
                 client_id='CLIENT_ID', client_secret="CLIENT_SECRET",
                 username='spiccymeatbot', password='PASSWORD')

subreddit = reddit.subreddit('spiccymeatballs')
for submission in subreddit.stream.submissions():
    # We work with submissions here. 
    random_number = random.randint(1, 100) # Pick a random number
    submission.reply(REPLY_STRING.format(str(random_number))) # Reply to the post