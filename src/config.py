import os


class Config(object):
    SLACK_URL = os.getenv("SLACK_URL", "")
    SLACK_TOKEN = os.getenv("SLACK_TOKEN", "")


config = Config
