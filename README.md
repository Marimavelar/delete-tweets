# delete-tweets

A fork of [Koenrh's delete-tweets](https://github.com/koenrh/delete-tweets). This README was adapted to my changes in the code. 

Remembering this code was modified for personal uses only :) 

This is a simple script that helps you delete tweets (or just replies or retweets) from your timeline. 

## Pre-requisites

1. A Twitter Developer account with elevated features. More information [here](https://developer.twitter.com/en/portal/products/elevated).

## Setup before using the script

1. Apply for a Twitter Developer account: 
    1. [Create a Twitter Developer account](https://developer.twitter.com/en/apply):
    2. Now wait for your Twitter Developer account to be reviewed and approved.
    3. Don't forget to apply for elevated features! :) 
2. Create a Twitter app
    1. [Create a new Twitter app](https://developer.twitter.com/en/apps/create) (not available as long as your Twitter Developer account is pending review).
    2. Enable OAuth 1.0A. 
        1. App permissions Read and Write
        2. Callback URL can be set to something like http://localhost if you are not going to implement sign-in for other users
        3. Website URL set to something valid like your blog ideally, or use http://example.com if you must
        4. Save and regenerate Access Token and Secret, now with read/write permission.
            > Remember that these permissions are for the account that owns the app only, you will not have access to write in other accounts. 
3. Configure your environment
    1. Open your Twitter Developer's [apps](https://developer.twitter.com/en/apps).
    2. Click the 'Details' button next to your newly created app.
    3. Click the 'Keys and tokens' tab, and find your keys, secret keys and access tokens.
    4. Now you need to make these keys and tokens available to your shell environment. Assuming you are using [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)):
      :warning: Before you continue, you should be aware that most shells record user
      input (and thus secrets) into a history file. In Bash you could prevent this by
      prepending your command with a _single space_ (requires `$HISTCONTROL` to be set
      to `ignorespace` or `ignoreboth`).

      ```bash
      export TWITTER_CONSUMER_KEY="your_consumer_key"
      export TWITTER_CONSUMER_SECRET="your_consumer_secret"
      export TWITTER_ACCESS_TOKEN="your_access_token"
      export TWITTER_ACCESS_TOKEN_SECRET="your_access_token_secret"
      ```
4. Get your tweet archive
    1. Open the [Your Twitter data page](https://twitter.com/settings/your_twitter_data)
    2. Scroll to the 'Download your Twitter data' section at the bottom of the page
    3. Re-enter your password
    4. Click 'Request data', and wait for the email to arrive
    5. Follow the link in the email to download your Tweet data
    6. Unpack the archive. The `tweet.js` file will be inside the data folder.
5. Install dependencies
    1. Make sure you have PIP (a Python package manager) installed:

        ```curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py```

    2. Now you can install all the library’s dependencies:

        ```pip install -r requirements.txt```

## Getting started

### Usage

Delete any tweet from _before_ January 1, 2022:

```bash
python3 deletetweets/__main__.py --until 2022-01-01 path_to_tweet.js
```

Or only delete all retweets:

```bash
python3 deletetweets/__main__.py --filter retweets path_to_tweet.js
```

### Spare tweets

You can optionally spare tweets by passing their id_str, setting a minimum amount of likes or retweets:

```bash
python3 deletetweets/__main__.py --until 2022-01-01 path_to_tweet.js --spare-ids 21235434 23498723 23498723
```

Spare tweets that have at least 10 likes, or 5 retweets:

```bash
python3 deletetweets/__main__.py --until 2022-01-01 path_to_tweet.js --spare-min-likes 10 --spare-min-retweets 5
```


## References 

[Twitter API v2 sample code](https://github.com/twitterdev/Twitter-API-v2-sample-code)

[Generate Twitter API Tokens with read/write Permissions](https://stackoverflow.com/questions/71439161/how-to-generate-twitter-api-access-token-and-secret-with-read-write-permission/71439483#71439483)

[Manage Tweets](https://developer.twitter.com/en/docs/twitter-api/tweets/manage-tweets/introduction)