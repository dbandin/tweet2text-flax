#!/usr/bin/env python3
"""
Small program to retrieve images from twitter and recognize text from images.
"""
# TODO: Make it modular.
from tweepy import OAuthHandler as twitter_oauth, API as twitter_api
from boto3 import client as boto_client
from requests import get
from argparse import ArgumentParser
from io import BytesIO, StringIO
from os import remove

# TODO: Add verifications if no AWS Keys are exported
# TODO: Add other options for twitter credentials.

def get_twitter_creds_yaml_file(twitter_creds_file):
    import yaml

    with open(twitter_creds_file, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    return cfg['twitter']

def parse_arguments():
    """
    Use argparse to handle cli arguments
    """
    # TODO: the cred file is a position required argument, it's a little bit contradictory
    # Define arguments.
    parser = ArgumentParser(description=__doc__)
    parser.add_argument(help="Url to specific twit to retrieve text", dest='tweet_url',
            metavar='TWITTER_URL', type=str)
    parser.add_argument('-t', '--twitter-cred-file', help="Path to YAML file with twitter credentials", dest='tweet_creds_file',
            metavar='TWITTER_CREDS_FILE', required=True, type=str)
    # parse arguments.
    args = parser.parse_args()
    return args.tweet_creds_file, args.tweet_url

def process_tweet_media(tweet):
    image_urls = get_image_url(tweet)

    if image_urls:
        print("## Tweet Image URL(s) ##")
        image_files = []
        for url in image_urls:
            print("\t{}".format(url))
            image_files.append(download_image(url)) 
        print("Image Local files: {}".format(image_files))
    
    process_images(image_files)


def process_images(image_list):
    for image in image_list:
        print("### Processing image ###")
        process_image(image)
        # Delete temporary image file
        remove(image)
    return True

def process_image(imageFile):
    # TODO: This method will required to be divided in smaller and less complex methods.
    client = boto_client('rekognition')
    # Open and read Image
    with open(imageFile, 'rb') as image:
        # response = client.detect_labels(Image={'Bytes': image.read()})
        image_stream = image.read()

    # Retrieve labels
    response = client.detect_labels(Image={'Bytes': image_stream})
    print('### Detected labels in image {} ###'.format(imageFile))
    for label in response['Labels']:
        print("{} : {}".format(label['Name'], str(label['Confidence'])))
    # Detect Text
    response = client.detect_text(Image={'Bytes': image_stream})

    textDetections=response['TextDetections']
    # print(response)
    print('### Detected text ###')
    # print(textDetections)
    detected_text = []
    for text in textDetections:
        detected_text.append(text['DetectedText'])
    print("Text Array: {}".format(detected_text))
    img_string = ''.join(detected_text).replace(' ','')
    print(img_string)

    if verify_if_binary(img_string):
        print("### Image contains binary code ###")
        decode_binary_string(img_string)

    return True


def decode_binary_string(image_string):
    image_string = '0b{}'.format(image_string)
    n = int(image_string,2)
    ascii_string = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()
    print("### Detected text traduction ###")
    print(ascii_string)


def verify_if_binary(input_string):
    str_set = set(input_string) 
    s = {'0', '1'} 

    if s == str_set or str_set == {'0'} or str_set == {'1'}: 
        return True
    else: 
        return False 


def download_image(url):
    filename = '/tmp/' + url.split('/')[-1]
    r = get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)

    return filename

def get_image_url(tweet):
    image_urls = []
    for media in tweet.entities['media']:
        if media['type'] == 'photo':
            image_urls.append(media['media_url_https'])
            
    return image_urls

def initialize_twitter_api(twitter_creds):
    # Creating the authentication object
    auth = twitter_oauth(twitter_creds['consumer_key'], twitter_creds['consumer_secret'])
    # Setting your access token and secret
    auth.set_access_token(twitter_creds['access_token'], twitter_creds['access_token_secret'])
    # Creating the API object while passing in auth information
    t_api = twitter_api(auth) 

    return t_api

def get_twiter_user_details(t_api, user):
    user = t_api.get_user(user)
    return user.screen_name, user.description

def parse_tweet_url(tweet_url):
    # Example URL: https://twitter.com/carolourdesm/status/1075791845773455360
    # TODO: work with shorturl links (Will need to actually retrieve it to identify the full tweet url after the redirect).
    # TODO: check that is actually a valid url, right now only splits the string.
    url_array = tweet_url.split("/")
    user = url_array[3]
    status = url_array[5]
    return user, status

def retrieve_single_tweet(t_api, tweet_status):
    # TODO: Add Exception handling
    tweet = t_api.get_status(tweet_status,tweet_mode='extended')
    return tweet



