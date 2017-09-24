import re
import logging
import json
import requests

def parse_message(request):
    data = json.loads(request.body)
    text = data['entry'][0]['messaging'][0]['message'].get('text')

    event_pattern = ".+[cC][uU][eE]\s(.+)\s[aA][tT]\s(.+)\s[aA][tT]\s(.+)$"
    event,time,location = re.findPattern(text, event_pattern)
