import get_lyrics
import random


def random_tweet(list):

    emojis = [' 💔 ', ' 💔💔 ', ' 🖤 ', ' 🦋', ' 🦋🦋 ']
    emoticons = [' *', ' ! ', ' !! ', ' *+ ', ' *! ',
                 ' +:) ', '* ', ' :) ', ' +', ' ** + ']
    last_char = [' !', ' *', ' ! *', ' .']

    old_tweet = list[random.randint(0, len(list) - 1)]
    new_tweet = ''

    if old_tweet[-1] == ",":
        old_tweet = old_tweet[:len(old_tweet) - 1]

    for i in range(len(old_tweet)):

        rand = random.randint(0, 10)

        if old_tweet[i] != " ":
            new_tweet += old_tweet[i]

        elif rand <= 5:
            new_tweet += ' '

        elif rand == 6:
            new_tweet += random.choice(emojis)
        else:
            new_tweet += random.choice(emoticons)

    new_tweet += random.choice(last_char)

    return new_tweet
