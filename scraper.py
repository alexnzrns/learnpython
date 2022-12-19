import snscrape.modules.twitter as sntwitter
import pandas as pd


query = "(#boykott) since:2022-11-24"
tweets = []

limit = 50

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit: 
      break
    else: 
      tweets.append([tweet.content])

print(tweets)

testdaten = pd.DataFrame(tweets, columns = ["text"])

testdaten.to_csv("out.csv", index=False)
