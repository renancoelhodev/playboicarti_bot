import tweepy
import lyrics_request
import time

consumer_key =  # DADOS PESSOAIS
consumer_secret =  # DADOS PESSOAIS
access_token =  # DADOS PESSOAIS
access_token_secret =  # DADOS PESSOAIS

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

for i in range(671):  # tweetar a cada 1 hora durante 4 semanas (período máximo para eu fazer o próximo update)
    api.update_status(lyrics_request.gerar_aleatorio())
    time.sleep(3600)
