from tweet2text import parse_tweet_url


def test_parse_tweet_url():
    tweet_url = 'https://twitter.com/carolourdesm/status/1075791845773455360'
    usr, stt = 'carolourdesm', '1075791845773455360'
    assert parse_tweet_url(tweet_url) == (usr, stt)
