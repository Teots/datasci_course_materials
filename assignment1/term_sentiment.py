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
    new_sentiments = {}
    for i in range(0, len(tweets)):
        if 'text' in tweets[i]:
            words = tweets[i]['text'].split(' ')
            sum = 0
            for word in words:
                if word in scores:
                    sum += scores[word]
            for word in words:
                if word not in scores:
                    if word in new_sentiments:
                        new_sentiments[word] = (float(sum) / float(len(words)) + new_sentiments[word]) / 2.0
                    else:
                        new_sentiments[word] = float(sum) / float(len(words))
    for k, v in new_sentiments.iteritems():
        print("%s %f" % (k, v))


if __name__ == '__main__':
    main()
