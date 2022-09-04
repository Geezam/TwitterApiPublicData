import tweepy

client = tweepy.Client("insert bearer token here")

user = "Geezam"

data = client.get_user(username=user,user_fields=["public_metrics"])

followers = data[0].public_metrics['followers_count']
following = data[0].public_metrics['following_count']
tweets = data[0].public_metrics['tweet_count']

print(user)
print(followers)
print(following)
print(tweets)

message = "Twitter user @" + str(user) + " has " \
+ str(followers) + " Followers, follows " \
+ str(following) + " accounts and has sent " \
+ str(tweets) + " Tweets."

print (message)
