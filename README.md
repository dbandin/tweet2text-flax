# tweet2text

Retrieve text from twitter and read text from images. From now it only translates binary text from the image, that was the test this was made to do, it may grow in the future if required.

# Installation

This package uses Python 3 a dependencies related to it. The dependencies can be installed beforehand with pip by example, but they are also defined in the setup.py file, so, if this package is installed with pip will retrieve the dependencies.

## Requirements

- Python 3
- Make your twitter account as developer account and generate some credentials to grant access to twitter to the script.
- Export AWS credentials in the session where the script is running or use an instance with a role with access to rekognition.

## Dependencies

- boto3
- tweepy
- argparse
- pyyaml

### Configuring deps using PIP and virtual env

If you have multiple versions of python running in your environments, I particularly like to use a virtual env, it's quite easy in that way.

~~~
 $ python3 -m venv p3_venv
~~~

The previous command creates a 'p3_venv' directory in your home.

Activating the python 3 enviornment.

~~~
 $ source ~/p3_venv/bin/activate
 (p3_venv) $
 Python 3.7.0
~~~

Install deps
~~~
 (p3_venv) $ pip install boto3 tweepy argparse
~~~

## Download the repo

~~~
 (p3_venv) $ git clone https://gitlab.com/dbandin/tweet2text.git
 (p3_venv) $ cd tweet2text
~~~

## Install locally the script.

~~~
 (p3_venv) $ pip install .
~~~

# Configuration

## Export AWS Credentials

If you are running it in a ec2 instance, you can use a role assigned to it with access to rekognition. Otherwise you can export in the shell session you are running some permanent or temporary credentials.
~~~
export AWS_ACCESS_KEY_ID="ASIASOMETHING"
export AWS_SECRET_ACCESS_KEY="...."
# THE SESSION TOKEN IS OPTIONAL, ONLY REQUIRED FOR TEMPORARY CREDENTIALS.
export AWS_SESSION_TOKEN="...."
~~~

## Twitter credentials

Add your twitter developer credentials to file twitter_credentials.yml under the cfg directory.
It's not necessary to place them in that path nor maintain that file name, it's just required to identify the file with the credentials argument.

# Running the script

CLI help/arguments.
~~~
 (p3_venv) $ tweet2txt --help
usage: tweet2txt [-h] -t TWITTER_CREDS_FILE TWITTER_URL

Small program to retrieve images from twitter and recognize text from images.

positional arguments:
  TWITTER_URL           Url to specific twit to retrieve text

optional arguments:
  -h, --help            show this help message and exit
  -t TWITTER_CREDS_FILE, --twitter-cred-file TWITTER_CREDS_FILE
                        Path to YAML file with twitter credentials
~~~

Example:
~~~
 (p3_venv) $ tweet2txt https://twitter.com/carolourdesm/status/1075791845773455360 -t ~/dev/twitter_credentials.yml 
Tweet url: https://twitter.com/carolourdesm/status/1075791845773455360
## User Details ##
	User: carolourdesm
	Screen Name: carolourdesm
	Description: Politóloga | Lic en Relaciones Internacionales 🌎 | 🕊
## Tweet Text ##
La misma tarjeta, el mismo deseo @DiegoBandin !
Espero que haya explotado el verano en Dublin!, El mejor de los regalos es Fausto 🧒🏽, espero pronto verte y conocer al pequeñin. https://t.co/TWGA4MXB7B
## Tweet Image URL(s) ##
	https://pbs.twimg.com/media/Du36khMWoAELNQZ.jpg
Image Local files: ['/tmp/Du36khMWoAELNQZ.jpg']
### Processing image ###
### Detected labels in image /tmp/Du36khMWoAELNQZ.jpg ###
Text : 91.15345764160156
Face : 59.536102294921875
Word : 55.9334716796875
Room : 55.531497955322266
Indoors : 55.531497955322266
### Detected text ###
Text Array: ['01001000 01 100001', '01110000 01110000', '01111001 00100000', '01000010 01101001', '01110010 01110100', '01101000 01100100', '01100001 01111001', '01001000', '01', '100001', '01110000', '01110000', '01111001', '00100000', '01000010', '01101001', '01110010', '01110100', '01101000', '01100100', '01100001', '01111001']
01001000011000010111000001110000011110010010000001000010011010010111001001110100011010000110010001100001011110010100100001100001011100000111000001111001001000000100001001101001011100100111010001101000011001000110000101111001
### Image contains binary code ###
### Detected text traduction ###
Happy BirthdayHappy Birthday
~~~

# TO-DO

This is the first ugly version that works, there is some exception handling, testing, inteligence and support to add.
