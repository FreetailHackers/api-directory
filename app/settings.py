# Code adapted from http://stevenloria.com/hosting-static-flask-sites-for-free-on-github-pages/
import os

DEBUG = True

# Assumes the app is located in the same directory
# where this file resides
APP_DIR = os.path.dirname(os.path.abspath(__file__))

def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))

# use relative URLs for GitHub
FREEZER_RELATIVE_URLS = True

PROJECT_ROOT = parent_dir(APP_DIR)
# In order to deploy to Github pages, deploying via the /docs directory
FREEZER_DESTINATION = PROJECT_ROOT + '/docs'
# Freezer will remove extra files it didn't generate, so the files listed
# below are the relevant code we need to keep.
FREEZER_DESTINATION_IGNORE = []
