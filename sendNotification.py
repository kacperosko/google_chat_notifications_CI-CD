"""
    @Author Kacper Osko (github @kacperosko)
    Send notification to Google Chat using API
"""

import sys
import argparse
from json import dumps
from httplib2 import Http
# Retrieve all setups
from settings import WEBHOOKS, PIPELINES_URL, COLOR_BLUE, COLOR_RED, COLOR_GREEN


def createMessage(args: argparse.Namespace, result='Processing') -> dict:
    """
    Create message in Google Chat format.

    :param args:
    :param result:
    :return:
    """

    if result == "Processing":
        color = COLOR_BLUE
    if result == "Success":
        color = COLOR_GREEN
    if result == "Failed":
        color = COLOR_RED

    # format text color to graphically show build status (blue, green, red)
    formatted_result = f'<font color=\"{color}\">' + result + '</font>'

    # Widget that contain current pipeline status
    args_status = {
        "keyValue": {
            "topLabel": "Deployment Status",
            "content": formatted_result
        }
    }

    # Widget that contain branch on which pipeline was triggered
    args_branch = {
        "keyValue": {
            "topLabel": "Target Branch",
            "content": args.branch
        }
    }

    # Widget that contain Full Name of person who triggered pipeline
    args_user = {
        "keyValue": {
            "topLabel": "User who triggered",
            "content": args.user
        }
    }

    args_url = f"{PIPELINES_URL}{args.buildnumber}"

    # Widget that contain a button with URL to triggered build
    open_pipeline_button = {
        "widgets": [{
            "buttons": [
                {
                    "textButton": {
                        "text": "OPEN PIPELINE",
                        "onClick": {
                            "openLink": {
                                "url": args_url
                            }
                        }
                    }
                }
            ]
        }]
    }

    # Connect all widgets together
    widgets = [args_branch, args_status]

    # Add User widget if User is given in command line
    if args.user is not None:
        widgets.append(args_user)

    JSON_TEMPLATE = {
        "cards": [
            {
                "header": {
                    "title": "DEPLOYMENT STATUS",
                },
                "sections": [
                    {
                        "widgets": widgets
                    },

                    open_pipeline_button if result != "Processing" else {}

                ]
            }
        ]
    }
    return JSON_TEMPLATE


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--exitcode", nargs='?', default='0', type=str, help="BITBUCKET_EXIT_CODE")
    parser.add_argument("-f", "--isbefore", nargs='?', default='n', type=str, help="Send message before running pipeline")
    parser.add_argument("-n", "--buildnumber", nargs='?', default='not-specified', type=str, help="BITBUCKET_BUILD_NUMBER")
    parser.add_argument("-b", "--branch", nargs='?', type=str, help="BITBUCKET_BRANCH")
    parser.add_argument("-u", "--user", nargs='?', type=str, help="USER_WHO_TRIGGERED_PIPELINE")

    args = parser.parse_args()

    print('>> DEBUG RECEIVED ARGS:', args)

    # To create a new thread in Google Chat You can use unique key, e.g. build number
    THREAD_KEY = args.buildnumber

    if args.exitcode != '':
        webhook = WEBHOOKS[args.branch]

        # Prepare Google Chat API endpoint
        url = f'https://chat.googleapis.com/v1/spaces/{webhook["GOOGLE_SPACE"]}/messages?key={webhook["GOOGLE_KEY"]}&token={webhook["GOOGLE_TOKEN"]}&thread_key={THREAD_KEY}'

        if args.isbefore == 'y':
            bot_message = createMessage(args)
        elif args.exitcode == '0':
            bot_message = createMessage(args, 'Success')
        else:
            bot_message = createMessage(args, 'Failed')

        message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
        http_obj = Http()

        # Send request to Google Chat API
        response, content = http_obj.request(
            uri=url,
            method='POST',
            headers=message_headers,
            body=dumps(bot_message),
        )

        print('>> DEBUG RECEIVED RESPONSE:', response)
        print('>> RESPONSE STATUS:', response.status)

        EXIT_CODE = 0
        # Return success or false for CI/CD interpreter
        if response.status == 200:
            EXIT_CODE = 1

        return EXIT_CODE


if __name__ == '__main__':
    main()
