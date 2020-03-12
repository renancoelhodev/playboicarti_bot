import requests
from bs4 import BeautifulSoup
import random

emojis = [' 💔 ', ' 💔💔 ', ' 🖤 ', ' 🖤🖤 ', ' 🐍 ', ' 🐍🐍 ', ' 🦋 ', ' 🦋🦋 ']
emoticons = [' * ', ' ** ', ' *+ ', ' *^ ', ' *! '
             ' + ', ' ++ ', ' +* ', ' +^ ', ' +! ',
             ' ^ ', ' ^^ ', ' ^* ', ' ^+ ', ' ^! ',
             ' ! ', ' !! ', ' !* ', ' !+ ', ' !^ ',
             ' <3 ', ' _ ']

vetor = []

url = ['https://www.cifraclub.com.br/playboi-carti/goku-asthma/letra/',
       'https://www.cifraclub.com.br/playboi-carti/broke-boi/letra/',
       'https://www.cifraclub.com.br/playboi-carti/fell-in-luv/letra/',
       'https://www.cifraclub.com.br/playboi-carti/lean-4-real/letra/',
       'https://www.cifraclub.com.br/playboi-carti/long-time-intro/letra/',
       'https://www.cifraclub.com.br/playboi-carti/molly/letra/',
       'https://www.cifraclub.com.br/playboi-carti/minute-maid/letra/',
       'https://www.cifraclub.com.br/playboi-carti/whole-lotta/letra/',
       'https://www.cifraclub.com.br/playboi-carti/new-choppa-feat-aap-rocky/letra/',
       'https://www.cifraclub.com.br/playboi-carti/right-now/letra/',
       'https://www.cifraclub.com.br/playboi-carti/location/letra/']


for i in url:
    res = requests.get(i)

    soup = BeautifulSoup(res.content, 'html.parser')

    letra = soup.find_all('div', class_='letra')

    for i in letra:
        lyrics = i.find_all('br')
        for j in lyrics:
            vetor.append(j.next_element)


def gerar_aleatorio():

    old_tweet = vetor[random.randint(0, len(vetor) - 1)]

    tweet = ''

    for i in range(len(old_tweet)):

        rand = random.randint(0, 10)

        if old_tweet[i] != " ":
            tweet += old_tweet[i]

        elif rand <= 5:
            tweet += ' '

        elif rand >= 8:
            tweet += random.choice(emojis)
        else:
            tweet += random.choice(emoticons)

    return tweet.lower()
