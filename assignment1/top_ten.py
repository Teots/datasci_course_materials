import sys
import json
import heapq


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
    hashtags = {}
    for tweet in tweets:
        if 'entities' in tweet:
            if 'hashtags' in tweet['entities']:
                for word in tweet['entities']['hashtags']:
                    if word['text'] in hashtags:
                        hashtags[word['text']] += 1
                    else:
                        hashtags[word['text']] = 1

    # Print the result
    for term, occ in sorted(hashtags.items(), key=lambda x: x[1], reverse=True)[:10]:
        print("%s %i" % (term, occ))

if __name__ == '__main__':
    main()
