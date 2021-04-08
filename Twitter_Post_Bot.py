import tweepy
import datetime
import time

# get required twitter API tokens from user keys.ini file and set to variables used for auth
with open('user keys.ini', 'r') as apiKeys:
    consumer_key = apiKeys.readline().split(" = ", 1)[1].split("\n")[0]
    consumer_secret = apiKeys.readline().split(" = ", 1)[1].split("\n")[0]
    access_token = apiKeys.readline().split(" = ", 1)[1].split("\n")[0]
    access_token_secret = apiKeys.readline().split(" = ", 1)[1].split("\n")[0]
    apiKeys.close()


# credentials for logging into twitter via API log in credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Tests auth. If the user name is printed, then auth is good.
user = api.me()
print('username:', user.name)
print('total followers:', user.followers_count)

# gets user # for twitch support account
twitch_support = api.get_user(id='@TwitchSupport')

# gets user # for twitch main account
twitch_main = api.get_user(id='Twitch')

# message that you want posted
message='  - @TwitchSupport My account was hacked and I provided info to get it back. Still no action or reply. Can I at least get my account deactivated so fraudulent charges can\'t be made? I can\'t log in. My password and email was changed! The email revert link didn\'t work!'


# function for getting the current time and posting the time + messafe
def status_bot():
    current_date = datetime.datetime.now().strftime('%a %H:%M')
    api.update_status(current_date + message)


# gets the amount of times the user wants to post a tweet and how often
# includes basic validation for hours / minute selection
timesToPost = input("Enter how many tweets you want to post: ")
timePer = input("Do you want to post every X minutes or hours? enter m/h ")
while True:
    if timePer.lower() == 'm':
        minutesPost = input("Enter how many minutes between posts you want: ")
        break
    elif timePer.lower() == 'h':
        minutesPost = input("Enter how many hours between posts you want: ")
        minutesPost *= 60
        break
    else:
        timePer = input("Do you want to post every X minutes or hours? enter m/h ")

# posts the tweet X amount of times ever Y minutes/hours
for x in range(int(timesToPost)):
    status_bot()
    print('status ' + str(x + 1) + ' posted')
    time.sleep(int(minutesPost) * 60)
