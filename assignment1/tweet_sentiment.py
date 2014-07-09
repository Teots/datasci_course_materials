import sys
import json


def parseAfinn():
    afinn_file = open(sys.argv[1])
    scores = {}
    for line in afinn_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores


def parseTwitter():
    tweet_file = open(sys.argv[2])
    tweets = []
    for line in tweet_file:
        tweets.append(json.loads(line))
    return tweets


def main():
    # Load the data
    scores = parseAfinn()
    tweets = parseTwitter()

    # Process the data
    for i in range(0, len(tweets)):
        if 'text' in tweets[i]:
            words = tweets[i]['text'].split(' ')
            sum = 0
            for word in words:
                if word in scores:
                    sum += scores[word]
            print(str(sum))

if __name__ == '__main__':
    main()
