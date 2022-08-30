# IMPORT
import requests

from config.testrail import APIClient

# ENVIRONMENT
production = ""
stagging = "https://api.staging.pintu.co.id"
sandbox = ""
use_env = stagging

# TESTRAIL
url = 'https://pintucrypto.testrail.io'
username = 'daffa@pintu.co.id'
password = '_Fawwaz170901_@@'
testRun = 61

# SLACK
slack_webhook = "https://hooks.slack.com/services/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"
slack_webhook_daffa = "https://hooks.slack.com/services/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"
slack_title = "Slack Api Automation"


def testrail_success(tc):
    client = APIClient(url)
    client.user = username
    client.password = password
    client.send_post(
        f'add_result_for_case/{testRun}/{tc}',
        {'status_id': 1, 'comment': 'Success, test by automation api'}
    )


def testrail_failed(tc):
    client = APIClient(url)
    client.user = username
    client.password = password
    client.send_post(
        f'add_result_for_case/{testRun}/{tc}',
        {'status_id': 5, 'comment': 'Failed, test by automation api'}
    )


def webhook_slack(color, success, failed, all, success_rate):
    sr = round(success_rate, 2)
    print(use_env)
    param = {
        "attachments": [
            {
                "color": color,
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": slack_title,
                            "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": f"*Success Test:*\n{success}"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Failed Test:*\n{failed}"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": "*Skipped Test:*\n0"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Total Test:*\n{all}"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "fields": [
                            {
                                "type": "mrkdwn",
                                "text": f"*Success Rate:*\n{sr}%"
                            },
                            {
                                "type": "mrkdwn",
                                "text": f"*Envi*\n{use_env}"
                            }
                        ]
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "<https://example.com|Check Detail Report>"
                        }
                    }
                ]
            }
        ]
    }
    header = {
        "content-type": "application/x-www-form-urlencoded"
    }
    requests.post(slack_webhook_daffa, json=param, headers=header)
