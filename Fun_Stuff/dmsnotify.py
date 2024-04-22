import json
from botocore.vendored import requests
import os

def lambda_handler(event, context):
    # Extract the EventBridge event detail
    event_detail = event['DMS Replication Task State Change']

    # Check if the detail contains an error
    if "error" in event_detail.lower():
        # Slack webhook URL (store it in Lambda environment variables for security)
        slack_webhook_url = 'https://hooks.slack.com/services/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'

        # Format the message for Slack
        slack_message = {
            "text": f"Error detected: {event_detail}"
        }

        # Send the message to Slack
        response = requests.post(slack_webhook_url, json=slack_message)

        # Check the response from Slack
        if response.status_code != 200:
            print(f"Failed to send message to Slack: {response.text}")
        else:
            print("Message sent to Slack successfully")
    else:
        print("No error found in the detail")

    return {
        'statusCode': 200,
        'body': json.dumps('Function executed successfully!')
    }
