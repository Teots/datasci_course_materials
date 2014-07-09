import sys
import json


def parse_twitter():
    tweet_file = open(sys.argv[1])
    tweets = []
    for line in tweet_file:
        tweets.append(json.loads(line))
    return tweets


def main():
    # Load the data
    tweets = parse_twitter()

    # Process the data
    tf = {}
    terms = 0
    for i in range(0, len(tweets)):
        if 'text' in tweets[i]:
            words = tweets[i]['text'].split()
            terms += len(words)
            for word in words:
                if word in tf:
                    tf[word] += 1
                else:
                    tf[word] = 1

    # Print the result
    for term, occ in tf.iteritems():
        print("%s %f" % (term, float(occ) / float(terms)))

if __name__ == '__main__':
    main()
