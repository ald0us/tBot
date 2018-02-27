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

        status_id = '412525863465680896' # target status_id
        
        respondTo = "@userName " # be sure to leave a space at the end or else comments wont post        
        try:
            if j[i]['POST'] == "True":
                api.update_status(respondTo + j[i]['COMMENT'], in_reply_to_status_id = status_id)
                print(j[i]['USER'], "Replied to status")

            api.create_favorite(status_id)
            print(j[i]['USER'], "Favorited Tweet")

            api.retweet(status_id)
            print(j[i]['USER'], "Retweeted")

            api.create_friendship(respondTo)
            print(j[i]['USER'], "Followed")

            print("\nPause for 2 seconds\n")
            time.sleep(2)

        except tweepy.TweepError as e:
            print(e.reason)

        except StopIteration:
            break
