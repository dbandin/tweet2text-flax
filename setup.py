import re
import os
import os.path
from setuptools import setup, find_packages

build = '0.2dev'


def __path(filename):
    return os.path.join(os.path.dirname(__file__),
                        filename)


if os.path.exists(__path('VERSION')):
    build = open(__path('VERSION')).read().strip()

REQUIREMENTS_FILE = "requirements/dev.in"

setup(name='tweet2text',
      version=build,
      description=("Read specific single status from twitter and dumps text"
                   " and text in image"),
      keywords='twitter tweet text translate binary ascii',
      url='https://gitlab.com/dbandin/tweet2text',
      author='Diego Bandin',
      author_email='dbandin@gmail.com',
      python_requires='>3.7',
      packages=find_packages(),
      install_requires=[a.strip() for a in filter(
          re.compile('^[a-zA-Z]').match, open(REQUIREMENTS_FILE))],
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points={
          'console_scripts': [
              'tweet2text = tweet2text.cli:main',
          ],
      },
      # scripts=['bin/tweet2txt'],
      include_package_data=True,
      zip_safe=False)
