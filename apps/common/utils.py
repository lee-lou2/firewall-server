import requests


def send_slack_message(webhook_url, message):
    requests.post(webhook_url, json={"text": message})
