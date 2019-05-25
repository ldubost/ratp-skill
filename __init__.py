from mycroft import MycroftSkill, intent_file_handler


class Ratp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ratp.intent')
    def handle_ratp(self, message):
        self.speak_dialog('ratp')


def create_skill():
    return Ratp()

