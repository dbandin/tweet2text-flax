#!/usr/bin/env python3

from tweet2text import (parse_arguments, parse_tweet_url, initialize_twitter_api,
    get_twiter_user_details, retrieve_single_tweet, process_tweet_media,
    get_twitter_creds_yaml_file)


def main():
    """
    Main program for cli interface.
    """
    # Call parse function to get the arguments necessary for the program to work.
    twitter_creds_file, tweet_url = parse_arguments()
    print("Tweet url: {}".format(tweet_url))
    t_user, t_status = parse_tweet_url(tweet_url)

    # TODO: Add other ways to use this credentials.
    twitter_creds = get_twitter_creds_yaml_file(twitter_creds_file)
    tweeter_api = initialize_twitter_api(twitter_creds)

    user_name, user_description = get_twiter_user_details(tweeter_api, t_user)
    tweet = retrieve_single_tweet(tweeter_api, t_status)

    print("## User Details ##\n\tUser: {}\n\tScreen Name: {}\n\tDescription: {}".format(t_user, user_name, user_description))
    print("## Tweet Text ##\n{}".format(tweet._json['full_text']))

    if 'media' in tweet.entities:
        process_tweet_media(tweet)

    return True


if __name__ == "__main__":
    exit(main())