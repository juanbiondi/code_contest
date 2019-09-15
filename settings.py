from os.path import join, dirname
from dotenv import load_dotenv
import os

# LOAD DOT ENV
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)


def str2bool(text):
    return (text is not None) and (text.lower() in ("yes", "true", "t", "1"))


class Settings:
    VERBOSE = os.environ.get('VERBOSE') == "True"

    MODEL_PATH = os.environ.get('MODEL_PATH')
    MODEL_URL = os.environ.get('MODEL_URL')
    USE_EXTERNAL = str2bool(os.environ.get('USE_EXTERNAL'))
