#Created app as admin
#Installed into workspace
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
        username="D04KP96AR7V",
        #token="xoxp-4682058257441-4662825083350-4694123818951-f3c27e56c93d0bb9d926efbf60cc431f",
        #burns token below
        #token="xoxp-4682058257441-4693124979344-4708729529458-a87fff731fced4238a5743495a7b0505",
        #text="Homer, your bravery and quick thinking have turned a potential Chernobyl into a mere Three-Mile Island. Bravo!  Now to celebrate lets get our webapp at http://www.springfieldpowerplant.com back up and running as quickly as possible, chop chop"
        text="Simpson!!!!  The website is down"
        #lisa
        #token="xoxp-4682058257441-4724932502290-4748651182960-3b7455bdbe82ad1b61e4e50bb282b062",
        #text="Dad...I mean Homer, I've been playing with this open source tool called Terraform and I think it can help provision out our infrastructure more quickly.  I setup a github repo with an example you can check out"

    )
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found'
