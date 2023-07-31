"""
    @Author Kacper Osko (github @kacperosko)
    File that is containing all setup required for sendNotification.py
"""


# Define URL for redirect button widget
PIPELINES_URL = "https://bitbucket.org/<your_domain>/<repository_name>/pipelines/results/"

# Define Your Google Chat Webhook. You can create multiple google spaces for each branch as below
WEBHOOKS = {
    # !!!!!!!!!!  Below are test value, replace with Your real ones (follow guide in README) !!!!!!!!!!
    "branch1": {"GOOGLE_KEY": "AAAAAAaaaAAAAAAAA-AAAAAAaaaAAAAAAAA",
                "GOOGLE_TOKEN": "V__AAAAAAaaaAAAAAAAAAAAAAAaaaAAAAAAAA", "GOOGLE_SPACE": "AAAAAAAAAAaaaAAA"},
    "branch2": {"GOOGLE_KEY": "AAAAAAaaaAAAAAAAA-AAAAAAaaaAAAAAAAA",
                "GOOGLE_TOKEN": "V__AAAAAAaaaAAAAAAAAAAAAAAaaaAAAAAAAA", "GOOGLE_SPACE": "AAAAAAAAAAaaaAAA"},
}

# Define Status colors
COLOR_BLUE = "#367be3"
COLOR_GREEN = "#39e650"
COLOR_RED = "#e83f10"
