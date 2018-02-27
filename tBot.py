import json
import tweepy
import time
with open('sdfsdf.json') as json_data:

    j = json.load(json_data)
    for i in range(2):
        i += 1
        i = str(i)
        CONSUMER_KEY = j[i]['CONSUMER_KEY']
        CONSUMER_SECRET = j[i]['CONSUMER_SECRET']
        ACCESS_TOKEN = j[i]['ACCESS_TOKEN']
        ACCESS_SECRET = j[i]['ACCESS_SECRET']
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
        api = tweepy.API(auth)

        list_id = '928188552910741505'

        api.update_status("@usernameToReplyTo this is another shot at this", in_reply_to_status_id = 928188552910741505)
        print(j[i]['USER'], "updated the status")

        api.create_favorite(list_id)
        print(j[i]['USER'], "favorited the tweet")

        api.retweet(list_id)
        print(j[i]['USER'], "retweeted the tweet")

        print("Pause for 2 seconds")
        time.sleep(2)



