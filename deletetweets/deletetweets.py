import io
import sys
import json
import time

from datetime import datetime
from dateutil import parser
from delete_tweet_twitter_api import deleteTweet

class TweetReader(object):
    def __init__(self, reader, since_date=None, until_date=None, filters=[], spare=[], min_likes=0, min_retweets=0):
        self.reader = reader
        self.since_date = datetime.min if since_date is None else parser.parse(since_date, ignoretz=True)
        self.until_date = datetime.now() if until_date is None else parser.parse(until_date, ignoretz=True)
        self.filters = filters
        self.spare = spare
        self.min_likes = 0 if min_likes is None else min_likes
        self.min_retweets = 0 if min_retweets is None else min_retweets

    def read(self):
        for row in self.reader:
            if row["tweet"].get("created_at", "") != "":
                tweet_date = parser.parse(row["tweet"]["created_at"], ignoretz=True)
                if tweet_date >= self.until_date or tweet_date <= self.since_date:
                    continue

            if ("retweets" in self.filters and
                    not row["tweet"].get("full_text").startswith("RT @")) or \
                    ("replies" in self.filters and
                     row["tweet"].get("in_reply_to_user_id_str") == ""):
                continue

            if row["tweet"].get("id_str") in self.spare:
                continue

            if (self.min_likes > 0 and int(row["tweet"].get("favorite_count")) >= self.min_likes) or \
                    (self.min_retweets > 0 and int(row["tweet"].get("retweet_count")) >= self.min_retweets):
                continue

            yield row


def delete(tweetjs_path, since_date, until_date, filters, s, min_l, min_r, dry_run=False):
    with io.open(tweetjs_path, mode="r", encoding="utf-8") as tweetjs_file:
        count = 1

        tweets = json.loads(tweetjs_file.read()[25:])
        for row in TweetReader(tweets, since_date, until_date, filters, s, min_l, min_r).read():
            deleteTweet(row["tweet"]["id_str"])
            count += 1
            rate_limit_count = count / 50
            if(rate_limit_count.is_integer() and rate_limit_count >= 6):
                print("15 minute sleep because of rate limit. Tweets already deleted: {}".format(count))
                time.sleep(900)
            elif():
                print("Over 300 requests done in 3 hours. Last tweet_id deleted was {}".format(row["tweet"]["id_str"]))
                sys.exit()


        print("Number of deleted tweets: %s\n" % count)

    sys.exit()
