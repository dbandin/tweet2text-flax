from setuptools import setup

setup(name='tweet2text',
      version='0.1',
      description="""
      Read specific single status from
      twitter and dumps text and text in image
      """,
      keywords='twitter tweet text translate binary ascii',
      url='https://github.com/dbandin/tweet2text-flax/',
      author='Diego Bandin',
      author_email='dbandin@gmail.com',
      packages=['tweet2text'],
      install_requires=[
          'tweepy',
          'argparse',
          'boto3',
          'pyyaml',
          'flask',
          'wtforms'
      ],
      test_suite='nose.collector',
      tests_require=['pytest'],
      include_package_data=True,
      zip_safe=False,
      setup_requires=['pytest_runner'],
      )
