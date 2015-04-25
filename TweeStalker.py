import tweepy
import time

# Consumer keys and access tokens, used for OAuth
consumer_key = '[consumer Key]'
consumer_secret = '[consumer secret]'
access_token = '[access token]'
access_token_secret = '[access token secret]'
 
# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
# Creation of the actual interface, using authentication
api = tweepy.API(auth)
 

user = api.get_user('7h3_j0k3r')
log_file = open('tweet_1.log', 'w')

print user.screen_name
log_file.write(user.screen_name + '\n')
log_file.write('----------------')
log_file.write(user.screen_name + ' has ' + str(user.followers_count) + ' followers' + '\n')
log_file.write('----------------' + '\n')


# Follow all the friends(followers) of above user
for friend in user.friends():
    log_file.write("Found _" + friend.screen_name + '\n')
    time.sleep(60)
    friend.follow()
    log_file.write("Following _" + friend.screen_name + '\n')
    user_x = api.get_user(friend.screen_name)
        
    for friend_x in user_x.friends():
          time.sleep(20)
          log_file.write("------------------" + '\n')
          log_file.write(friend_x.screen_name + '\n')
          log_file.write("------------------" + '\n')
          friend_x.follow()
          #print api.retweet(friend_x.screen_name)
          log_file.write("-- Following --" + friend_x.screen_name + '\n') 

    time.sleep(10)

log_file.close()
