# -*- coding: utf-8 -*-

"""{Description}"""

__author__ = "k.mp"

# generic | built-in imports
import os

# project imports
from dotenv import load_dotenv


# load dotenv file
load_dotenv()

# Application base directory
basedir = os.path.abspath(os.path.dirname(__file__))


class Settings(object):

    # Secret key
    SECRET_KEY = os.getenv("SECRET_KEY") or "kg"

    # Debugging
    DEBUG = os.getenv("DEBUG") or True


if __name__ == "__main__":
    print(basedir)