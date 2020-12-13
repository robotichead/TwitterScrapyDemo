import scrapy, time, sys, schedule

# Global Variables
saved_tweets = []
first_run = True
username = input("What is the user's name?: ")


def ShowFirstFiveTweets(tweet_text):
    for index, tweet in enumerate(tweet_text):
        # Check to make sure we do not show more than 5 tweets
        if index >= 5:
            break

        sys.stdout.write('\n\n\n%s' % tweet)
        sys.stdout.flush()

        # Add tweets to the saved_tweets array
        saved_tweets.append(tweet)


def ShowNewestTweets(tweet_text):
    for tweet in tweet_text:
        # If the tweet does not already exist in saved tweets print them
        if not tweet in saved_tweets:
            sys.stdout.write('\n\n\n%s' % tweet)
            sys.stdout.flush()
        else:
            # Break out of this
            break


class TwitterSpider(scrapy.Spider):
    name = "twitter"
    download_delay = 4

    def start_requests(self):
        urls = [
            'https://mobile.twitter.com/%s' % username,
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

        # First run has been completed
        first_run = False

        """
        # The following has been commented out as it causes the whole terminal to lock up
        while(True):
            time.sleep(600)
            for url in urls:
                yield scrapy.Request(url=url, callback=self.parse)
        """


    def parse(self, response):
        tweet_text = response.xpath('//*[contains(@class,"dir-ltr")]').getall()

        # Depending if we are running for the first time depends if we are showing new tweets or the first 5
        if first_run:
            ShowFirstFiveTweets(tweet_text)
        else:
            ShowNewestTweets(tweet_text)
