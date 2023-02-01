import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = "xoxb-4682058257441-4701511450149-n7vWyLmIG4HvFWdZVRtJQNv8"
#slack_token = os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=slack_token)

try:
    response = client.chat_postMessage(
        channel="C04LQ7LBFJP",
        text="Simpson!  The web site is down!"
    )
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found'
