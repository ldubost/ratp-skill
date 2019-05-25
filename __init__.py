import json, requests, urllib
from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.log import getLogger

baseurl = "http://api-ratp.pierre-grimaud.fr/v3/schedules/"
linetype = "bus"
line = "72"
station = "Lamballe-Ankara"
destination = "R"
introText = "The next passage is"

LOGGER = getLogger(__name__)

class Ratp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ratp.intent')
    def handle_ratp(self, message):
        LOGGER.info("here")
        url = baseurl + linetype + "/" + line + "/" + urllib.parse.quote(station) + "/" + destination
        LOGGER.info("URL: " + url)
        resp = requests.get(url=url)
        LOGGER.info("Result: " + resp.text)
        data = json.loads(resp.text)
        str = introText

        for dest in data["result"]["schedules"]: 
            str+= " " + dest["message"].replace("mn", "minutes").replace("A l'approche", "coming")
            str+= " " + dest["destination"]
        self.speak(str)


def create_skill():
    return Ratp()

