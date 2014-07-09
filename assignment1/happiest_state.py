import sys
import json


states = {
    'AK': 'Alaska',
    'AL': 'Alabama',
    'AR': 'Arkansas',
    'AS': 'American Samoa',
    'AZ': 'Arizona',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DC': 'District of Columbia',
    'DE': 'Delaware',
    'FL': 'Florida',
    'GA': 'Georgia',
    'GU': 'Guam',
    'HI': 'Hawaii',
    'IA': 'Iowa',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'MA': 'Massachusetts',
    'MD': 'Maryland',
    'ME': 'Maine',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MO': 'Missouri',
    'MP': 'Northern Mariana Islands',
    'MS': 'Mississippi',
    'MT': 'Montana',
    'NA': 'National',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'NE': 'Nebraska',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NV': 'Nevada',
    'NY': 'New York',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'PR': 'Puerto Rico',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VA': 'Virginia',
    'VI': 'Virgin Islands',
    'VT': 'Vermont',
    'WA': 'Washington',
    'WI': 'Wisconsin',
    'WV': 'West Virginia',
    'WY': 'Wyoming'
}


def parse_afinn():
    afinn_file = open(sys.argv[1])
    scores = {}
    for line in afinn_file:
        term, score = line.split("\t")
        scores[term] = int(score)
    return scores


def parse_twitter():
    tweet_file = open(sys.argv[2])
    tweets = []
    for line in tweet_file:
        tweets.append(json.loads(line))
    return tweets


def main():
    # Load the data
    scores = parse_afinn()
    tweets = parse_twitter()

    # Process the data
    happyness = {}
    for tweet in tweets:
        # Calculate the sentiment score of the tweet
        if 'text' in tweet:
            words = tweet['text'].split()
            total = 0
            for word in words:
                if word in scores:
                    total += scores[word]
            # Get the state this tweet originates from
            if 'place' in tweet and tweet['place'] is not None:
                if 'full_name' in tweet['place'] and tweet['place']['full_name'] is not None:
                    locations = tweet['place']['full_name'].split()
                    for location in locations:
                        if location in states:
                            if location in happyness:
                                happyness[location] += total
                            else:
                                happyness[location] = total
                        break
            elif 'user' in tweet and tweet['user'] is not None:
                if 'location' in tweet['user'] and tweet['user']['location'] is not None:
                    locations = tweet['user']['location'].split()
                    for location in locations:
                        if location in states:
                            if location in happyness:
                                happyness[location] += total
                            else:
                                happyness[location] = total
                        break
    # Print the result
    happiest_state = states.keys()[0]
    happiest_value = -sys.maxint - 1
    for k, v in happyness.iteritems():
        if v > happiest_value:
            happiest_state = k

    print(happiest_state)

if __name__ == '__main__':
    main()
