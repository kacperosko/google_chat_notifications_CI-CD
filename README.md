# Python notifications to Google Chat for CI/CD

This python script will send notification to Google Chat Space before running build and after with showing its result. You can include name of user who triggered build.

## Features

- Define multiple webhooks for each branches (seperate Google Chat spaces)
- Get full name of User who triggered build (bitbucket)
- Simple adjustment to Your CI/CD process

## Requirement

**Google Chat Notidications CI/CD** is using:

- Python 3.10
- Python Packages:
  - argparse
  - httplib2
- <a href="https://developers.google.com/chat/how-tos/webhooks" target="_blank">Google Chat webhook</a>

## Installation

Download repository and install requirements
```commandline
git clone https://github.com/kacperosko/google_chat_notifications_CI-CD.git
cd google_chat_notifications_CI-CD
pip install -r requirements.txt
```
Create webhook in Google Chat following instruction:<br>
<a href="https://developers.google.com/chat/how-tos/webhooks#create_a_webhook" target="_blank">Create a webhook</a>

Then add **KEY** and **TOKEN** in python script inside dictionary **webhooks** with branch as dict key.
### Example configured webhooks in [settings.py](settings.py)
```python
webhooks = {
        "develop": {"GOOGLE_KEY":   "AAAAAAaaaAAAAAAAA-AAAAAAaaaAAAAAAAA",
                    "GOOGLE_TOKEN": "V__AAAAAAaaaAAAAAAAAAAAAAAaaaAAAAAAAA",
                    "GOOGLE_SPACE": "AAAAAAAAAAaaaAAA"},
  
        "production": {"GOOGLE_KEY":   "BBBbbbBbBbbbBBB-BBBbbbBbBbbbBBB",
                       "GOOGLE_TOKEN": "V__BBBbbbBbBbbbBBBBBBbbbBbBbbbBBB",
                       "GOOGLE_SPACE": "BBBbbbBbBbbbBBB"},
    }
```

Run command inside **google_chat_notifications_CI-CD** folder to test it

```commandline
python3 sendNotifaction.py --exitcode 1 --isbefore n --buildnumber 1234 --branch develop --user "Kacper Osko"
```

## Usage

```commandline
python3 sendNotifaction.py -h
              
>> usage: sendNotification.py [-h] [-e [EXITCODE]] [-f [ISBEFORE]] [-n [BUILDNUMBER]] [-b [BRANCH]] [-u [USER]]
>>
>> options:
   -h, --help                       show this help message and exit
  -e [EXITCODE], --exitcode         [EXITCODE]
                                    BITBUCKET_EXIT_CODE
  -f [ISBEFORE], --isbefore         [ISBEFORE]
                                    Send message before running pipeline
  -n [BUILDNUMBER], --buildnumber   [BUILDNUMBER]
                                    BITBUCKET_BUILD_NUMBER
  -b [BRANCH], --branch             [BRANCH]
                                    BITBUCKET_BRANCH
  -u [USER], --user                 [USER]
                                    USER_WHO_TRIGGERED_PIPELINE
```

## Example
You can find example usage in file [example-bitbucket-pipeline.yml](example-bitbucket-pipeline.yml)<br>
It is already configured for Bitbucket CI/CD.


## License

MIT

**Free Software, Have fun! :D**

